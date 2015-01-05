# -*- coding: utf-8 -*-
from django.db import models

# Año de la diversificacion productiva y del fortalecimiento de la educacion
# Create your models here.
class General(models.Model):
	codigo_padrino = models.CharField(max_length=8)
	nombre_padrino = models.CharField(max_length=100)
	apellidos_padrino = models.CharField(max_length=100)
	sede_padrino = models.CharField(max_length=20)
	
	situacion = models.CharField(max_length=8, choices=SITUACION)
	ruta = models.CharField(max_length=8, choices=RUTA)
	numero = models.CharField(max_length=5, blank=True)
	prenombre = models.CharField(max_length=160, choices=PRENOMBRE)
	nombre = models.CharField(max_length=200)
	escuela_ghp = models.CharField(max_length=160, choices=SINO)
	nivel = models.CharField(max_length=100, choices=NIVEL)
	codigo_ghp = models.CharField(max_length=5)
	direccion = models.CharField(max_length=200)
	poblacion = models.CharField(max_length=50)
	distrito = models.CharField(max_length=50)
	provincia = models.CharField(max_length=50)
	departamento = models.CharField(max_length=50)
	ugel = models.CharField(max_length=100, blank=True)
	fecha_de_registro = models.DateField()
	msnm = models.PositiveSmallIntegerField()
	director = models.CharField(max_length=200, blank=True)
	dni = models.CharField(max_length=8, blank=True)
	usuario_siagie = models.CharField(max_length=50, blank=True)
	password_siagie = models.CharField(max_length=50, blank=True)
	celular = models.CharField(max_length=200, blank=True)
	nro_computadoras = models.PositiveSmallIntegerField(blank=True)
	nro_laptops = models.PositiveSmallIntegerField(blank=True)
	con_qaliwarma = models.CharField(max_length=200, blank=True, choices=SINO)
	quintil_de_probreza = models.CharField(max_length=15, choices=QUINTIL)
	num_docentes = models.PositiveSmallIntegerField(blank=True)
	num_secciones = models.PositiveSmallIntegerField(blank=True)

	def __unicode__(self):
		return self.codmod

	class Admin:
		pass