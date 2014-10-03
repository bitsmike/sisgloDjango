from django.db import models

# Create your models here.
class Departamento(models.Model):
	cod_departamento = models.CharField(max_length=2, primary_key=True)
	name_departamento = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name_departamento

class Provincia(models.Model):
	cod_provincia = models.CharField(max_length=4, primary_key=True)
	name_provincia = models.CharField(max_length=100)
	departamento = models.ForeignKey(Departamento)

	def __unicode__(self):
		return self.name_provincia

	class Admin:
		pass
		
class Distrito(models.Model):
	cod_distrito = models.CharField(max_length=6, primary_key=True)
	name_distrito = models.CharField(max_length=100)
	provincia = models.ForeignKey(Provincia)
	departamento = models.ForeignKey(Departamento)
	#cps = models.ManyToManyField(Cenpob,  through_fields=('distrito','cenpob'))

	def __unicode__(self):
		return self.name_distrito

class Centro_poblado(models.Model):
	codigo_cenpob = models.CharField(max_length=6, primary_key=True)
	nombre_cenpob = models.CharField(max_length=100)
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
	cp_dis_prov_dep = models.CharField(max_length=200)
	dep_prov_dis_cp = models.CharField(max_length=200)

	# personalizamos el titulo de lo que se quiere mostrar
	# def Distrito_Cenpob (self):
	# 	return self.cod_dist.name_distrito
	# Distrito_Cenpob.admin_order_field = 'cod_dist__name_distrito'

	def __unicode__(self):
		return self.name_cenpob