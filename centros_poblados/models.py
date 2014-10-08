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

	class Admin:
		pass


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
	def _Distrito (self):
		return self.distrito.name_distrito
	_Distrito.admin_order_field = 'distrito__name_distrito'

	def _Provincia (self):
		return self.provincia.name_provincia
	_Provincia.admin_order_field = 'provincia__name_provincia'

	def _Departamento (self):
		return self.departamento.name_departamento
	_Departamento.admin_order_field = 'departamento__name_departamento'

	def __unicode__(self):
		return self.nombre_cenpob

	class Admin:
		pass
