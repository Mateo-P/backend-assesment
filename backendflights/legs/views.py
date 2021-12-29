from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from .models import Leg
from .serializers import LegSerializer
from rest_framework.permissions import IsAuthenticated

class LegViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated)
    serializer_class = LegSerializer
    queryset = Leg.objects.all()