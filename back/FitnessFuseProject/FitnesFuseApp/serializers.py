from rest_framework import serializers
from FitnesFuseApp.models import Weight, Steps, ClaoriseBurned, Training

class WeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weight
        fields = ['id', 'user','weight',
                  'measurement_date',
                  ]

class StepsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Steps
        fields = ['user', 'steps',
                  'measurement_date']

class ClaoriseBurnedSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClaoriseBurned
        fields = ['user', 'kcal',
                  'measurement_date']

class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = ['user', 'training',
                  'training_time', 'measurement_date']
