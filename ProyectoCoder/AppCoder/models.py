from django.db import models
from django.contrib.auth.models import User
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

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)
    
    def __str__(self):
        
        return f"{self.user} - {self.imagen}"