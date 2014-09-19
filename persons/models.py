#encoding:utf-8
from django.db import models
from photos.models import Photo
from cenpobs.models	import Cenpob
from distritos.models import Distrito
from provincia

# Create your models here.
class Person(models.Model):
	dni = models.CharField(max_length=8, blank=True, unique=True)
	first_name = models.CharField(max_length=60)
	last_name = models.CharField(max_length=80)
	fecnac = models.DateField(blank=True)
	gender = models.CharField(max_length=1)
	address = models.CharField(max_length=180)
	neighborhood = models.CharField(max_length=100)

	cell1 = models.CharField(max_length=9, blank=True)
	cell2 = models.CharField(max_length=9, blank=True)
	email = models.EmailField(blank=True)
	person_photo = models.ForeignKey(Photo, blank=True)