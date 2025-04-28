from rest_framework.routers import DefaultRouter
from .views import GlucoseEntryViewSet, MealViewSet, ActivityViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'glucose', GlucoseEntryViewSet)
router.register(r'meals', MealViewSet)
router.register(r'activities', ActivityViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
