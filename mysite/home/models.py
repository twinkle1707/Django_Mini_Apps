from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField(null=True , blank = True)
    image = models.ImageField(null=True)
    file = models.FileField(null=True)

class Product(models.Model):
    pass

