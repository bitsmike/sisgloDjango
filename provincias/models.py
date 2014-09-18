#encoding:utf-8
from django.db import models
from departamentos.models import Departamento

# Create your models here.
class Provincia(models.Model):
	cod_provincia = models.CharField(max_length=4, primary_key=True)
	name_provincia = models.CharField(max_length=100)
	dep = models.ForeignKey(Departamento)

	def __unicode__(self):
		return self.name_provincia