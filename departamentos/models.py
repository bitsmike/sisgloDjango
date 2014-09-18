#encoding:utf-8
from django.db import models

# Create your models here.
class Departamento(models.Model):
	cod_departamento = models.CharField(max_length=2, primary_key=True)
	name_departamento = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name_departamento