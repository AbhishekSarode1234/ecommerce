from django.db import models

# Create your models here.

class Product(models.Model):
    def __str__(self) -> str:
        return self.title
    
    title = models.CharField(max_length=255)
    price = models.FloatField()
    discount = models.FloatField()
    category = models.CharField(max_length=255)
    description=models.TextField(max_length=255)
    image = models.CharField(max_length=400)

class User(models.Model):
    def __str__(self) -> str:
        return self.username
    
    username = models.CharField(max_length=200) 
    email = models.CharField(max_length=200)
    password=models.CharField(max_length=200)