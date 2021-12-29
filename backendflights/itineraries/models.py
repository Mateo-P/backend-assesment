from django.db import models
from agents.models import Agent


class Itinerary(models.Model):
    id = models.CharField(primary_key=True, max_length=60)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    agent = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f'{self.id}'