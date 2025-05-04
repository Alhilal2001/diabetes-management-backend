# backend/main_app/serializers.py

from rest_framework import serializers
from .models import GlucoseEntry, Meal, Activity
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
        
class GlucoseEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = GlucoseEntry
        fields = ['id', 'glucose_level', 'timestamp']


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ['id', 'name', 'carbs', 'timestamp']


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'name', 'duration', 'timestamp']
