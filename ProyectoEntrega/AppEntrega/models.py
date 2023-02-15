from django.db import models

# Create your models here.

class usuario(models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    email= models.EmailField()

class truco(models.Model):
    nombre= models.CharField(max_length=40)
    clase= models.CharField(max_length=30)

class magos(models.Model):
    nombre= models.CharField(max_length=40) 
    apellido= models.CharField(max_length=40)
    