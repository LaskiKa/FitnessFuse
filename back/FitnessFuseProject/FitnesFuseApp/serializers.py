from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers
from FitnesFuseApp.models import Weight, Steps, ClaoriseBurned, Training
from rest_framework.authtoken.models import Token


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],
                                        validated_data['email'],
                                        validated_data['password'])
        Token.objects.create(user=user)
        return user


class LoginUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')

class WeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weight
        fields = ['id', 'user', 'weight',
                  'measurement_date',
                  ]


class StepsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Steps
        fields = ['id', 'user', 'steps',
                  'measurement_date']


class ClaoriseBurnedSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClaoriseBurned
        fields = ['id', 'user', 'kcal',
                  'measurement_date']


class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = ['user', 'training',
                  'training_time', 'measurement_date']
