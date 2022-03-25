from rest_framework.serializers import ModelSerializer
from properties.models import Property

# TODO: Permissions
class PropertySerializer(ModelSerializer):
    class Meta:
        model = Property
        fields = "__all__"