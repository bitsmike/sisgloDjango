#encoding:utf-8
from django.db import models

# Create your models here.
class Photo(models.Model):
	photoname = models.CharField(max_length=255)
	photodatetime = models.DateTimeField()
	#photoimage = models.ImageField(upload_to='photos')