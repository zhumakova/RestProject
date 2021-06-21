from django.contrib.auth import authenticate, login
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

    def put(self, request):
        profile = Profile.objects.get(user=request.user)
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('OK', status=200)
        return Response(serializer.errors, status=400)

    def delete(self, request):
        profile = Profile.objects.get(user=request.user)
        profile.delete()
        return Response('DELETED', status=200)

class RegisterView(APIView):

    def post(self,request,*args,**kwargs):
        serializer=RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Successfuly registered!',status=201)
        return Response(serializer.errors,status=400)

class LoginView(APIView):
    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.data.get('username')
            password = serializer.data.get('password')
            user = authenticate(username=username,password=password)
            login(request,user)
            return Response('welcome')
        return Response(serializer.errors)

