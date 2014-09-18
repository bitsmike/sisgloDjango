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

	def __unicode__(self):
		return self.name_cenpob