from django.db import models

# Create your models here.
class Municipio(models.Model):
	municipio_coordinacion = models.CharField(max_length=45, unique=True)

	def __unicode__(self):
		return self.municipio_coordinacion