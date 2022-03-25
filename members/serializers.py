from rest_framework.serializers import ModelSerializer

from members.models import Member


class MemberSerializer(ModelSerializer):
    class Meta:
        model = Member 
        exclude = ('password', 'email',)
