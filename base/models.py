from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Product(models.Model):
    user =models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    image = models.ImageField(null=True,blank=True,default='/placeholder.png')
    price = models.FloatField()
    description = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
   
    def __str__(self):
        return self.title