from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    email= models.EmailField()
    def __str__(self):
        return self.nombre + " " + self.apellido+ " " + self.email

class Truco(models.Model):
    nombre= models.CharField(max_length=40)
    clase= models.CharField(max_length=30)

    def __str__(self):
        return self.nombre + '' + self.clase 

class Mago(models.Model):
    nombre= models.CharField(max_length=40) 
    apellido= models.CharField(max_length=40)
    def __str__(self):
        return self.nombre + " " + self.apellido
        
class Estilo(models.Model):
    nombre= models.CharField(max_length=40) 
    def __str__(self):
        return self.nombre 