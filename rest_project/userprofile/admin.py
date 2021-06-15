from django.contrib import admin
from .models import *

class ProfileAdmin(admin.ModelAdmin):
    list_display=['photo','full_name','email','address','count_order','wallet','sale']
admin.site.register(Profile,ProfileAdmin)
