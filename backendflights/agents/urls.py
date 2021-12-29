from rest_framework import urlpatterns
from .views import AgentViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'',AgentViewSet,basename='Agents')

urlpatterns = [path('', include(router.urls))]