#encoding:utf-8
from django.db import models
from persons.models import Person

# Create your models here.
class Course(models.Model):
	grado = models.CharField(max_length=10)
	seccion = models.CharField(max_length=10)
	courseTeacher = models.ForeignKey(Person)