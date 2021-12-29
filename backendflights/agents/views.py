from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from .models import Agent
from .serializers import AgentSerializer
from rest_framework.permissions import IsAuthenticated

class AgentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated)
    serializer_class = AgentSerializer
    queryset = Agent.objects.all()