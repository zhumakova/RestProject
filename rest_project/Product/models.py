from django.db import models

class Category(models.Model):
    title=models.CharField(max_length=50)

    def __str__(self):
        return self.title
class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    photo=models.ImageField(blank=True,null=True)
    name=models.CharField(max_length=50)
    price=models.FloatField(default=0.0)
    desc=models.TextField()
    avg_score=models.FloatField(default=0.0)

    def __str__(self):
        return self.name
