from django.db import models
from itineraries.models import Itinerary
from agents.models import Agent

class Leg(models.Model):
    id = models.CharField(primary_key=True, max_length=60)
    departure_airport = models.CharField(max_length=3)
    arrival_airport = models.CharField(max_length=3)
    agent = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True)
    departure_time = models.DateField()
    arrival_time = models.DateField()
    stops = models.IntegerField(default=0)
    duration_mins = models.IntegerField
    itinerary = models.ForeignKey(Itinerary, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.id}'