#encoding:utf-8
from django.db import models
# from cenpobs.models import Cenpob
# from distritos.models import Distrito
# from provincias.models import Provincia
# from municipios.models import Municipio
# from departamentos.models import Departamento

# Create your models here.
class Departamento(models.Model):
	cod_departamento = models.CharField(max_length=2, primary_key=True)
	name_departamento = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name_departamento


class Provincia(models.Model):
	cod_provincia = models.CharField(max_length=4, primary_key=True)
	name_provincia = models.CharField(max_length=100)
	dep = models.ForeignKey(Departamento)

	def __unicode__(self):
		return self.name_provincia


class Distrito(models.Model):
	cod_distrito = models.CharField(max_length=6, primary_key=True)
	name_distrito = models.CharField(max_length=100)
	prov = models.ForeignKey(Provincia)
	#cps = models.ManyToManyField(Cenpob,  through_fields=('distrito','cenpob'))

	def __unicode__(self):
		return self.name_distrito


class Ubication(models.Model):
	Codigo_Ubication = models.CharField(max_length=12, primary_key=True, unique=True)
	pais = models.CharField(max_length=20, default='PERU')
	departamento = models.ForeignKey(Departamento)
	provincia = models.ForeignKey(Provincia)
	distrito = models.ForeignKey(Distrito)
	Centro_poblado = models.ForeignKey(Cenpob)
	# estos dos campos se utlizaran para agilizar las busquedas
	cp_dis_prov_dep = models.CharField(max_length=200)
	dep_prov_dis_cp = models.CharField(max_length=200)

	def __unicode__(self):
		return self.Centro_poblado.name_cenpob+' - '+self.distrito.name_distrito+' - '+self.provincia.name_provincia
