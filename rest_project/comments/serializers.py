from rest_framework import serializers
from .models import Comment,Product,Rate

class CommentSerializer(serializers.Serializer):
    text=serializers.CharField()

class ProductDetailSerializer(serializers.ModelSerializer):
    comment_set=CommentSerializer(many=True)
    class Meta:
        model=Product
        fields=['id','photo','name','desc','price','avg_score','category','comment_set']
class RateSerializer(serializers.Serializer):
    score=serializers.FloatField(min_value=1.0,max_value=5.0)