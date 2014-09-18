#encoding:utf-8
from django.db import models
from persons.models import Person
from courses.models import Course

# Create your models here.
class Condicion(models.Model):
	estado = models.CharField(max_length=9)
	motivo_estado = models.CharField(max_length=20)

class Student(models.Model):
	cod_student = models.CharField(max_length=11, blank=True)
	studentPerson = models.ForeignKey(Person)
	studentCourse = models.ForeignKey(Course)
	estado_estudent = models.ForeignKey(Condicion)
	notas = models.TextField()

