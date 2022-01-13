from django.db import models
from django.core.validators import MinValueValidator


class Agent(models.Model):
    name = models.CharField(max_length=32)
    rating = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f'{self.name}'

class Airline(models.Model):
    api_id = models.CharField(max_length=60)
    name = models.CharField(max_length=60)

    def __str__(self):
        return f'{self.name}'
class Leg(models.Model):
    api_id = models.CharField( max_length=60)
    departure_airport = models.CharField(max_length=3)
    arrival_airport = models.CharField(max_length=3)
    airline = models.ForeignKey(Airline, on_delete= models.DO_NOTHING)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    stops = models.IntegerField(default=0)
    duration_mins = models.IntegerField(default=0)


    def __str__(self):
        return f'from: {self.departure_airport} to: {self.arrival_airport} duration: {self.duration_mins}mins'

class Itinerary(models.Model):
    api_id = models.CharField(max_length=60)
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    agent = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True)
    legs = models.ManyToManyField(Leg)

    def __str__(self):
        return f'price: {self.price} agent: {self.currency}'
