from rest_framework.serializers import ModelSerializer
from landlords.models import Landlord

# TODO: permissions 
class LandlordSerializer(ModelSerializer):
    class Meta:
        model = Landlord
        fields = '__all__'