from django.urls import path
from .views import *

urlpatterns=[
   path('product_detail/<int:product_id>/',ProductDetailView.as_view(),name='product_detail'),
   path('score/<int:product_id>/',RatePostView.as_view(),name='score')
 ]