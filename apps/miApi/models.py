from django.db import models

# Create your models here.
class Producto2 (models.Model):
    codigo = models.CharField(max_length=10)
    producto = models.CharField(max_length=50)
    precio = models.CharField(max_length=12)
    marca = models.CharField(max_length=30)
