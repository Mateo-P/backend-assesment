from django.db.models import fields
from rest_framework import serializers
from .models import Leg


class LegSerializer(serializers.ModelSerializer):

    class Meta:
        model = Leg
        fields = '__all__'