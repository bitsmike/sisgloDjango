# -*-encoding:utf-8 -*-
from django.db import models
from centros_poblados.models import Centro_poblado

# Create your models here.
class Persona(models.Model):
	dni = models.CharField(max_length=8, blank=True, unique=True)
	nombres = models.CharField(max_length=60)
	apellidos = models.CharField(max_length=80)
	fecnac = models.DateField(blank=True)
	sexo = models.CharField(max_length=1)
	direccion = models.CharField(max_length=180)
	barrio = models.CharField(max_length=100)
	ubicacion = models.Foreignkey(Centro_poblado)
	celular1 = models.CharField(max_length=9, blank=True)
	celular2 = models.CharField(max_length=9, blank=True)
	email = models.EmailField(blank=True)