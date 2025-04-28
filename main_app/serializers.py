from rest_framework import serializers
from .models import GlucoseEntry, Meal, Activity

class GlucoseEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = GlucoseEntry
        fields = '__all__'

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = '__all__'

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'
