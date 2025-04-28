from django.db import models
from django.contrib.auth.models import User

class GlucoseEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    glucose_level = models.IntegerField()
    prediction = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.glucose_level} mg/dL"

class Meal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    carbs = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.description[:30]}..."

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=100)
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.type} - {self.duration} mins"
