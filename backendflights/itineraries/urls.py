
from django.views.generic import base
from .views import AgentViewSet,AirlineViewSet, LegViewSet, ItinerayList, InfoLoad
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'agents', AgentViewSet, basename='Agents')
router.register(r'airlines', AirlineViewSet, basename='Airlines')
router.register(r'legs', LegViewSet, basename='Legs')


urlpatterns = [
    path('', include(router.urls)),
    path('loadinfo/', InfoLoad.as_view()),
    path('itineraries/', ItinerayList.as_view())
]
