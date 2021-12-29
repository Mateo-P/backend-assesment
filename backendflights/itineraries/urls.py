from .views import ItinerayViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', ItinerayViewSet, basename='Itineraries')

urlpatterns = [
    path('', include(router.urls)),
]
