from django.db import models
from datetime import*

# Create your models here.

class Miembro(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    edad= models.IntegerField()
    afinidad= models.CharField(max_length=50)
    fecha_nacimiento= models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.nombre} - {self.afinidad}"

class Colaborador(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    dni= models.IntegerField()
    cargo= models.CharField(max_length=50)
    fecha_ingreso= models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.nombre} - {self.cargo}"
    
class Producto(models.Model):
    nombre= models.CharField(max_length=50)
    marca= models.CharField(max_length=50)
    codigo= models.IntegerField()
    cantidad= models.IntegerField()
    fecha_registro= models.DateField(null=True, blank=True)
    
    def __str__(self) -> str:
        return f"{self.nombre} - {self.marca}"
    