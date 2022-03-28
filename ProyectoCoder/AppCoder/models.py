from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    contraseña= models.CharField(max_length=15)


class Deportes(models.Model):
    nombre= models.CharField(max_length=30)
    categoria= models.CharField(max_length=30)
    comentario= models.CharField(max_length=120)

class Politica(models.Model):
    nombre= models.CharField(max_length=30)
    categoria= models.CharField(max_length=30)
    comentario= models.CharField(max_length=120)

class Arte(models.Model):
    nombre= models.CharField(max_length=30)
    categoria= models.CharField(max_length=30)
    comentario= models.CharField(max_length=120)