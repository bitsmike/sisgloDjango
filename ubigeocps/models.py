#encoding:utf-8
from django.db import models
from cenpobs.models import Cenpob
from distritos.models import Distrito
from provincias.models import Provincia
from municipios.models import Municipio
from departamentos.models import Departamento

# Create your models here.
class Ubigeocp(models.Model):
	Codigo_Ubigeocp = models.CharField(max_length=12, primary_key=True, unique=True)
	pais = models.CharField(max_length=20, default='PERU')
	departamento = models.ForeignKey(Departamento)
	provincia = models.ForeignKey(Provincia)
	distrito = models.ForeignKey(Distrito)
	Centro_poblado = models.ForeignKey(Cenpob)
	#municipio_coordinacion = models.ForeignKey(Municipio)
	# estos dos campos se utlizaran para agilizar las busquedas
	cp_dis_prov_dep = models.CharField(max_length=250, default='wiii')
	dep_prov_dis_cp = models.CharField(max_length=250, default='wiii')

	def __unicode__(self):
		return self.Centro_poblado.name_cenpob+' - '+self.distrito.name_distrito+' - '+self.provincia.name_provincia