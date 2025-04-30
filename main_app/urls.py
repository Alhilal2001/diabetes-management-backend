# backend/main_app/urls.py

from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # Authentication
    path('auth/signup/', views.SignupView.as_view(), name='signup'),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Glucose
    path('glucose/', views.GlucoseListCreateView.as_view(), name='glucose-list'),
    path('glucose/<int:pk>/', views.GlucoseRetrieveUpdateDestroyView.as_view(), name='glucose-detail'),

    # Meals
    path('meals/', views.MealListCreateView.as_view(), name='meal-list'),
    path('meals/<int:pk>/', views.MealRetrieveUpdateDestroyView.as_view(), name='meal-detail'),

    # Activities
    path('activities/', views.ActivityListCreateView.as_view(), name='activity-list'),
    path('activities/<int:pk>/', views.ActivityRetrieveUpdateDestroyView.as_view(), name='activity-detail'),
]
