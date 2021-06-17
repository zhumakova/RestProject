from django.contrib import admin
from .models import *

class OrderAdmin(admin.ModelAdmin):
    list_display = ['product',
    'profile',
    'quantity' ,
    'date_created',
    'status','total_sum']
    readonly_fields = ['date_created','total_sum','profile']

admin.site.register(Order,OrderAdmin)
