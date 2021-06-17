from django.urls import path
from .views import *

urlpatterns=[
    path('order/',OrderPostView.as_view())
]