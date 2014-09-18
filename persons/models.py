#encoding:utf-8
from django.db import models
from photos.models import Photo
from ubigeocps.models import Ubigeocp

# Create your models here.
class Gender(models.Model):
	name_gender = models.CharField(max_length=20)

class Person(models.Model):
	dni = models.CharField(max_length=8, blank=True, unique=True)
	paternal = models.CharField(max_length=45)
	maternal = models.CharField(max_length=45, blank=True)
	first_name = models.CharField(max_length=60)
	fecnac = models.DateField(blank=True)
	gender = models.ForeignKey(Gender)
	address = models.CharField(max_length=250)
	neighborhood = models.CharField(max_length=100)
	cell1 = models.CharField(max_length=9, blank=True)
	cell2 = models.CharField(max_length=9, blank=True)
	person_photo = models.ForeignKey(Photo, blank=True)
	person_ubigeocp = models.ForeignKey(Ubigeocp)
	email = models.EmailField()