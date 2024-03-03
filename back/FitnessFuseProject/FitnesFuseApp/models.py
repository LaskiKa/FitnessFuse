from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Weight(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    weight = models.SmallIntegerField(default=0)
    measurement_date = models.DateTimeField()
    update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.weight} - {self.measurement_date}"

class Steps(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    steps = models.IntegerField(blank=True, default=0)
    measurement_date = models.DateTimeField()
    update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.steps} - {self.measurement_date}"

class ClaoriseBurned(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    kcal = models.IntegerField(blank=True, default=0)
    measurement_date = models.DateTimeField()
    update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.kcal} - {self.measurement_date}"

class Training(models.Model):
    TRAINING_CHOICES = [
        ('strength', 'Strength'),
        ('running', 'Running'),
        ('walk', 'Walk'),
        ('cycling', 'Cycling'),
        ('cardio', 'Cardio'),
        ('flexibility', 'Flexibility'),
        ('endurance', 'Endurance'),
        ('balance', 'Balance'),
        ('ergometr', 'Ergometr')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    training = models.CharField(choices=TRAINING_CHOICES)
    training_time = models.DurationField()
    measurement_date = models.DateTimeField()
    update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.training} - {self.measurement_date}"