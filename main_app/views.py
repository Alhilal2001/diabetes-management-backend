from rest_framework import viewsets
from .models import GlucoseEntry, Meal, Activity
from .serializers import GlucoseEntrySerializer, MealSerializer, ActivitySerializer
from rest_framework.permissions import IsAuthenticated

class GlucoseEntryViewSet(viewsets.ModelViewSet):
    queryset = GlucoseEntry.objects.all()
    serializer_class = GlucoseEntrySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
