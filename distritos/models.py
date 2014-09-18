#encoding:utf-8
from django.db import models
from provincias.models import Provincia
#from cenpobs.models import Cenpob

# Create your models here.
class Distrito(models.Model):
	cod_distrito = models.CharField(max_length=6, primary_key=True)
	name_distrito = models.CharField(max_length=100)
	prov = models.ForeignKey(Provincia)
	#cps = models.ManyToManyField(Cenpob,  through_fields=('distrito','cenpob'))

	def __unicode__(self):
		return self.name_distrito