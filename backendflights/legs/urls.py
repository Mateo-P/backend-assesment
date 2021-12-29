from .views import LegViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', LegViewSet, basename='Legs')

urlpatterns = [
    path('', include(router.urls)),
]
