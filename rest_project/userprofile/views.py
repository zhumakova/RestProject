from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *

class ProfileView(APIView):

    def get(self,request):
        try:
            profile=Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            return Response('404',status=status.HTTP_404_NOT_FOUND)
        serializer=ProfileSerializer(profile)
        return Response(serializer.data,status=status.HTTP_200_OK)