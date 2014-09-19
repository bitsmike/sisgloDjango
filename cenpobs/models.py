#encoding:utf-8
from django.db import models
from distritos.models import Distrito

# Create your models here.
class Cenpob(models.Model):
	cod_cenpob = models.CharField(max_length=6, primary_key=True)
	name_cenpob = models.CharField(max_length=100)
	con_ie = models.CharField(max_length=1)
	nivel_ie = models.CharField(max_length=9, blank=True)
	fuente_g = models.CharField(max_length=45)
	msnm = models.CharField(max_length=4)
	XGD = models.CharField(max_length=20)
	YGD = models.CharField(max_length=20)
	cod_dist = models.ForeignKey(Distrito)

	#personalizamos el titulo de lo que se quiere mostrar
	def Distrito_Cenpob (self):
		return self.cod_dist.name_distrito
	Distrito_Cenpob.admin_order_field = 'cod_dist__name_distrito'

	def __unicode__(self):
		return self.name_cenpob