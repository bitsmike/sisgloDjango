# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.
# SEDES = (
# 	("SPAIN","ESPAÑA"),
# 	('ITALY','ITALIA'),
# )

class Padrino(models.Model):
	cod_padrino = models.CharField(max_length=6)
	nombres = models.CharField(max_length=60)
	apellidos = models.CharField(max_length=60)
	sede = models.CharField(max_length=60)

	def __unicode__(self):
		return self.nombres

	class Admin:
		pass