from django.shortcuts import render
from django.utils import timezone
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

class MyOrderView(APIView):
    def get(self, request):
        profile = request.user.profile
        orders = profile.orders.all()
        serializer = MyOrderSerializer(orders, many=True)
        return Response(serializer.data)

class UpdateDeleteOrder(APIView):
    def put(self,request,*args,**kwargs):
        order=Order.objects.get(id=kwargs['order_id'])
        order_date=order.date_created
        order_status=order.status
        date_now=timezone.now()
        delta=timezone.timedelta(minutes=10)
        serializer=OrderSerializer(order,data=request.data)
        if (date_now-order_date)<=delta and order_status=='in_process':
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        return Response('Time is up!')

