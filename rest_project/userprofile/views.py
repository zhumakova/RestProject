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

class RegisterView(APIView):

    def post(self,request,*args,**kwargs):
        serializer=RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Successfuly registered!',status=201)
        return Response(serializer.errors,status=400)

