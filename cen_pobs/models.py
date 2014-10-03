# encoding:utf-8
from django.db import models
from distritos.models import Distrito
from provincias.models import Provincia
from municipios.models import Municipio
from departamentos.models import Departamento

# Create your models here.
class Cen_pob(models.Model):
	Codigo_cenpob = models.CharField(max_length=6, primary_key=True, unique=True)
	name_cenpob = models.CharField(max_length=100)
	con_ie = models.CharField(max_length=1)
	nivel_ie = models.CharField(max_length=9, blank=True)
	fuente_g = models.CharField(max_length=45)
	msnm = models.CharField(max_length=4)
	XGD = models.CharField(max_length=20)
	YGD = models.CharField(max_length=20)
	distrito = models.ForeignKey(Distrito)
	provincia = models.ForeignKey(Provincia)
	departamento = models.ForeignKey(Departamento)
	pais = models.CharField(max_length=20, default='PERU')
	# estos dos campos se utlizaran para agilizar las busquedas
	cp_dis_prov_dep = models.CharField(max_length=200)
	dep_prov_dis_cp = models.CharField(max_length=200)

	def __unicode__(self):
		# return self.Centro_poblado.name_cenpob+' - '+self.distrito.name_distrito+' - '+self.provincia.name_provincia
		return self.name_cenpob