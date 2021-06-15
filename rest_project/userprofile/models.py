from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    full_name=models.CharField(max_length=50)
    email=models.EmailField()
    address=models.CharField(max_length=150)
    wallet=models.PositiveIntegerField(default=0)
    photo=models.ImageField(null=True,blank=True)
    count_order=models.PositiveIntegerField(default=0)
    sale=models.FloatField(default=0.0)

    def __str__(self):
        return self.full_name
