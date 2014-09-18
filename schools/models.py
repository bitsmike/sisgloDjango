#encoding:utf-8
from django.db import models
from persons.models import Person

# Create your models here.
class SchoolMinEdu(models.Model):
	codmod = models.CharField(max_length=7)
	name_school = models.CharField(max_length=150)
	levelmode = models.CharField(max_length=45)
	address = models.CharField(max_length=250)
	distrit = models.CharField(max_length=100)
	province  = models.CharField(max_length=100)
	departament = models.CharField(max_length=100)
	
class SchoolGhp(models.Model):
	numero = models.CharField(max_length=6)
	cod_escuela = models.CharField(max_length=5)
	can = models.CharField(max_length=2)
	escuelaminedu = models.ForeignKey(SchoolMinEdu)
	director = models.ForeignKey(Person)
