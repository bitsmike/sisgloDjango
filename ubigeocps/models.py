#encoding:utf-8
from django.db import models

# Create your models here.
class Ubigeocp(models.Model):
	ubigeo = models.CharField(max_length=6)
	departamento = models.CharField(max_length=100)
	provincia = models.CharField(max_length=100)
	distrito = models.CharField(max_length=100)
	codcp = models.CharField(max_length=6)
	cenpob = models.CharField(max_length=100)
	con_ie = models.CharField(max_length=1)
	nivel_ie = models.CharField(max_length=9, blank=True)
	fuente_g = models.CharField(max_length=45)
	msnm = models.CharField(max_length=4)
	XGD = models.CharField(max_length=20)
	YGD = models.CharField(max_length=20)

	def __unicode__(self):
		return self.ubigeo