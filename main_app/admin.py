from django.contrib import admin
from .models import GlucoseEntry, Meal, Activity

admin.site.register(GlucoseEntry)
admin.site.register(Meal)
admin.site.register(Activity)

