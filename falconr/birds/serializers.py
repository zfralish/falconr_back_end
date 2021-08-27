from rest_framework import serializers
from .models import Bird, Hunt, Weight, Training, Feeding


class BirdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bird
        fields = '__all__'


class HuntSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hunt
        fields = '__all__'


class WeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weight
        fields = '__all__'


class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = '__all__'


class FeedingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feeding
        fields = '__all__'
