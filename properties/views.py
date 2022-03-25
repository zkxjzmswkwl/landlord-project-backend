from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from properties.models import Property
from properties.serializers import PropertySerializer


class PropertyViewSet(ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer