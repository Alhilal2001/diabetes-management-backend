from django.test import TestCase
from django.contrib.auth.models import User
from main_app.models import GlucoseEntry, Meal, Activity
from datetime import datetime

class DiaTrackModelsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='diapatient', password='secure123')

        self.glucose1 = GlucoseEntry.objects.create(user=self.user, glucose_level=180, timestamp=datetime(2024, 5, 1, 10, 0))
        self.glucose2 = GlucoseEntry.objects.create(user=self.user, glucose_level=220, timestamp=datetime(2024, 5, 2, 12, 0))

        self.meal1 = Meal.objects.create(user=self.user, name="Breakfast", carbs=45, timestamp=datetime(2024, 5, 1, 8, 0))
        self.meal2 = Meal.objects.create(user=self.user, name="Lunch", carbs=60, timestamp=datetime(2024, 5, 1, 13, 0))

        self.activity1 = Activity.objects.create(user=self.user, name="Jogging", duration=30, timestamp=datetime(2024, 5, 1, 9, 0))
        self.activity2 = Activity.objects.create(user=self.user, name="Yoga", duration=45, timestamp=datetime(2024, 5, 2, 18, 0))

    def test_glucose_creation(self):
        self.assertEqual(self.glucose1.glucose_level, 180)
        self.assertEqual(self.glucose1.user.username, 'diapatient')

    def test_meal_creation(self):
        self.assertEqual(self.meal1.name, 'Breakfast')
        self.assertEqual(self.meal1.carbs, 45)

    def test_activity_creation(self):
        self.assertEqual(self.activity1.name, 'Jogging')
        self.assertEqual(self.activity1.duration, 30)

    def test_user_relationships(self):
        self.assertEqual(self.user.glucoseentry_set.count(), 2)
        self.assertEqual(self.user.meal_set.count(), 2)
        self.assertEqual(self.user.activity_set.count(), 2)

    def test_cascade_delete_user(self):
        self.user.delete()
        self.assertEqual(GlucoseEntry.objects.count(), 0)
        self.assertEqual(Meal.objects.count(), 0)
        self.assertEqual(Activity.objects.count(), 0)
