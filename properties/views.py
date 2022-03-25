from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from properties.models import Property
from properties.serializers import PropertySerializer


class PropertyViewSet(ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    # TODO: Sort properties by landlord id
    @action(detail=False, methods=["GET"])
    def sort(self, request):
        pass