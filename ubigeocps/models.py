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
	Centro_poblado = models.ForeignKey(Cenpob)
	distrito = models.ForeignKey(Distrito)
	provincia = models.ForeignKey(Provincia)
	municipio = models.ForeignKey(Municipio)
	departamento = models.ForeignKey(Departamento)
	pais = models.CharField(max_length=20, default='PERU')

	def __unicode__(self):
		return self.Centro_poblado.name_cenpob+' - '+self.distrito.name_distrito+' - '+self.provincia.name_provincia