import datetime
import random

from django.utils import timezone

from ..models import Bird, Weight, Feeding, Hunt, Training


def generate_feeding_weights(date_delta, bird, training_length: int, hunts: int):
    bird = Bird.objects.get(pk=bird)
    for i in range(0, date_delta + 1):
        post_feed_time = timezone.now() - datetime.timedelta(days=i)
        feed_time = post_feed_time - datetime.timedelta(minutes=15)
        pre_feed_time = feed_time - datetime.timedelta(hours=1)
        late_weight = Weight(mass=950, time=post_feed_time, bird=bird)
        feeding = Feeding(type='Squirrel', mass=50, time=feed_time, bird=bird)
        early_weight = Weight(mass=900, time=pre_feed_time, bird=bird)
        if i > date_delta - hunts:
            hunt = Hunt(
                start_time=pre_feed_time,
                end_time=post_feed_time,
                game='Squirrel',
                performance=random.randint(0, 10),
                kills=random.randint(0, 5),
                bird=bird,
                notes='Great'
            )
            hunt.save()
        if not (i > training_length):
            if i > training_length // 2:
                type_train = 'Creance Flights'
            else:
                type_train = 'Hop ups'
            train = Training(
                start_time=pre_feed_time,
                end_time=post_feed_time,
                training_type=type_train,
                performance=random.randint(0, 10),
                bird=bird,
                notes='good boi'
            )
            train.save()
        late_weight.save()
        feeding.save()
        early_weight.save()
