# -*- coding: utf-8 -*-

from django.db import models
from centros_poblados.models import Centro_poblado

SITUACION = (
	("ACTIVO","ACTIVO"),
	('INACTIVO','INACTIVO'),
)

RUTA = (
	('RUTA 01', 'RUTA 01'),
	('RUTA 02', 'RUTA 02'),
	('RUTA 03', 'RUTA 03'),
	('RUTA 04', 'RUTA 04'),
	('RUTA 05', 'RUTA 05'),
	('RUTA 06', 'RUTA 06'),
	('RUTA 07', 'RUTA 07'),
	('RUTA 08', 'RUTA 08'),
	('RUTA 09', 'RUTA 09'),
	('RUTA 10', 'RUTA 10'),
	('RUTA 11', 'RUTA 11'),
	('RUTA 12', 'RUTA 12'),
	('RUTA 13', 'RUTA 13'),
	('RUTA 14', 'RUTA 14'),
	('RUTA 15', 'RUTA 15'),
	('RUTA 16', 'RUTA 16'),
	('RUTA 17', 'RUTA 17'),
	('OTRO', 'OTRO'),
)

NIVEL = (
	('PRIMARIA','PRIMARIA'),
	('INICIAL','INICIAL'),
	('SECUNDARIA','SECUNDARIA'),
	('SUPERIOR','SUPERIOR'),
	('CETPRO','CETPRO'),
	('OTRO','OTRO'),
)

SINO = (
	('SI','SI'),
	('NO','NO'),
)

QUINTIL = (
	('1','1'),
	('2','2'),
	('3','3'),
	('4','4'),
	('5','5'),
	('INDETERMINADO','INDETERMINADO'),
)

PRENOMBRE = (
	('PRONOEI','PRONOEI'),
	('INICIAL','INICIAL'),
	('IEP','IEP'),
	('IEP-NO ESCOLARIZADO','IEP-NO ESCOLARIZADO'),
	('IES','IES'),
	('IES-NO ESCOLARIZADO','IES-NO ESCOLARIZADO'),
	('CEBA','CEBA'),
	('IST','IST'),
	('ISPT','ISPT'),
	('ESFA','ESFA'),
	('CETPRO','CETPRO'),
	('CEO','CEO'),
	('CEO-CETPRO','CEO-CETPRO'),
	('CEO-ARTESANAL','CEO-ARTESANAL'),
)

# Create your models here.
class Escuela(models.Model):
	codmod = models.CharField(max_length=7, primary_key=True)
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