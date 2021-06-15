from django.shortcuts import render
from rest_framework.response import  Response
from rest_framework import status
from .serializers import *
from rest_framework.views import APIView

class CategoryView(APIView):

    def get(self,request):
        category=Category.objects.all()
        serializer=CategorySerializer(category,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


