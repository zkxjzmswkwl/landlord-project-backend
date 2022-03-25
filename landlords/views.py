from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from landlords.serializers import LandlordSerializer
from landlords.models import Landlord


class LandlordViewSet(ModelViewSet):
    queryset = Landlord.objects.all()
    serializer_class = LandlordSerializer