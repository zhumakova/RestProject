from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model=Product
        fields='__all__'

class CategorySerializer(serializers.ModelSerializer):
    product_set=ProductSerializer(many=True)

    class Meta:
        model=Category
        fields=['id','title','product_set']