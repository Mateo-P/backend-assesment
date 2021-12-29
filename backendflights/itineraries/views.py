from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from .models import Agent
from .serializers import ItinerarySerializer
from rest_framework.permissions import IsAuthenticated

class ItinerayViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated)
    serializer_class = ItinerarySerializer
    queryset = Agent.objects.all()