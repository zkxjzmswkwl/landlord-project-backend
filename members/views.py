from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from members.models import Member
from members.serializers import MemberSerializer


class MemberViewSet(ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    @action(detail=False, methods=["GET"])
    def find_reyzrs_mom(self, request):
        queryset = Member.objects.filter(reyzrs_mom=True)
        return Response(MemberSerializer(instance=queryset, many=True).data)