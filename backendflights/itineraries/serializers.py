from django.db.models import fields
from rest_framework import serializers
from .models import Agent, Airline, Leg, Itinerary

class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = '__all__'


class AirlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airline
        fields = '__all__'
class LegSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leg
        fields = '__all__'

class ItinerarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Itinerary
        fields = '__all__'