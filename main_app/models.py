# backend/main_app/models.py

from django.db import models
from django.contrib.auth.models import User

class GlucoseEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    glucose_level = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.glucose_level} mg/dL - {self.timestamp.date()}"


class Meal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    carbs = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.carbs}g carbs"


class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    duration = models.IntegerField(help_text="Duration in minutes")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.duration} mins"
