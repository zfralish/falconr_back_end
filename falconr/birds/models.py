from django.db import models
from django.db.models import Avg
from falconr.users.models import User
import datetime
import uuid
import statistics


# Create your models here.
class UUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class Bird(UUIDModel):
    name = models.CharField(max_length=20)
    trap_weight = models.FloatField()
    trap_date = models.DateTimeField(auto_now_add=True, null=True)
    species = models.CharField(max_length=100)
    sex = models.CharField(max_length=10)

    # falconer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='birds')

    @property
    def avg_weight(self):
        return self.weights \
            .filter(time__lte=datetime.datetime.today(),
                    time__gt=datetime.datetime.today() - datetime.timedelta(days=14)).aggregate(Avg('mass'))

    @property
    def hourly_weight_loss(self):
        weights = self.weights.filter(time__lte=datetime.datetime.today(),
                                      time__gt=datetime.datetime.today() - datetime.timedelta(days=14)).values_list()
        avgs = []
        for i in range(0, len(weights)):
            feeding_count = self.feedings.filter(time__lte=weights[i][2], time__gt=weights[i+1][2])
            mass_1 = weights[i].mass
            if not i + 1 < len(weights):
                break
            else:
                mass_2 = weights[i+1].mass

            if (mass_1 < mass_2) and feeding_count < 1:
                time_diff = weights[i].time - weights[i+1].time
                time_diff = time_diff.seconds / 3600
                weight_diff = (mass_2 - mass_1) / time_diff
                avgs.append(weight_diff)

        return statistics.mean(avgs)


class Weight(UUIDModel):
    mass = models.FloatField()
    time = models.DateTimeField()
    bird = models.ForeignKey(Bird, on_delete=models.CASCADE, related_name='weights')

    class Meta:
        ordering = ['-time']


class Feeding(UUIDModel):
    type = models.CharField(max_length=20)
    mass = models.FloatField()
    time = models.DateTimeField()
    bird = models.ForeignKey(Bird, on_delete=models.CASCADE, related_name='feedings')

    class Meta:
        ordering = ['-time']


class Hunt(UUIDModel):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    game = models.CharField(max_length=25)
    performance = models.IntegerField()
    kills = models.IntegerField()
    bird = models.ForeignKey(Bird, on_delete=models.CASCADE, related_name='hunts')
    notes = models.TextField()

    class Meta:
        ordering = ['-start_time']


class Training(UUIDModel):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    training_type = models.CharField(max_length=50)
    performance = models.IntegerField()
    bird = models.ForeignKey(Bird, on_delete=models.CASCADE, related_name='trainings')
    notes = models.TextField()

    class Meta:
        ordering = ['-start_time']