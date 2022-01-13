#from rest_framework.decorators import permission_classes
#from rest_framework.permissions import IsAuthenticated
#from .task import data_load_info

import django_filters
from rest_framework import (
    viewsets, status, generics
)
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Agent, Airline, Leg, Itinerary
from .serializers import AgentSerializer,AirlineSerializer, LegSerializer, ItinerarySerializer
from utils.dataload import load_json
from utils.parse_legs import parse_legs
from utils.parse_itineraries import parse_itineraries
from rest_framework import generics

class InfoLoad(APIView):
    def post(self,_):
        data = load_json()
        legs, itineraries = data['legs'], data['itineraries']
        parse_legs(legs, Leg, Airline) 
        parse_itineraries(itineraries, Itinerary,Agent,Leg)
        return Response(data,status=status.HTTP_201_CREATED)


class AgentViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated)
    serializer_class = AgentSerializer
    queryset = Agent.objects.all()


class AirlineViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated)
    serializer_class = AirlineSerializer
    queryset = Airline.objects.all()

class LegViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated)
    serializer_class = LegSerializer
    queryset = Leg.objects.all()


class ItineraryFilter(django_filters.FilterSet):
    agent = django_filters.CharFilter(field_name="agent__name")
    min_agent_rating = django_filters.NumberFilter(field_name="agent__rating", lookup_expr='gte')
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Itinerary
        fields = ['api_id', 'min_price', 'max_price','min_agent_rating', 'agent']
        
class ItinerayList(generics.ListAPIView):
    queryset = Itinerary.objects.all()
    #permission_classes = (IsAuthenticated)
    serializer_class = ItinerarySerializer
    filter_class = ItineraryFilter
    
