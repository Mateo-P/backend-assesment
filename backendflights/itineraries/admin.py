from django.contrib import admin

from .models import Agent, Airline, Leg, Itinerary
# Register your models here.
admin.site.register(Agent)
admin.site.register(Airline)
admin.site.register(Leg)
admin.site.register(Itinerary)
