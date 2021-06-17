from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *

class OrderPostView(APIView):

    def post(self,request,*args,**kwargs):
        #product=Product.objects.get(id=kwargs['product']
        #profile=request.user.profile
        serializer=OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)