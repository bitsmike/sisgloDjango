# -*- coding: utf-8 -*-
from django.db import models
from escuelas.models import Escuela
from centros_poblados.models import Centro_poblado
from datetime import datetime
from django.shortcuts import render_to_response
import MySQLdb
 
# db = MySQLdb.connect(user='root', db='db_sisglo', passwd='', host='127.0.0.1')
# cursor = db.cursor()
# cursor.execute('SELECT * FROM generals_general ORDER BY codigo_inicial')
# names = [row[0] for row in cursor.fetchall()]
# db.close()
# return render_to_response('book_list.html', {'names': names})


SEXO = (
	('M','MASCULINO'),
	('F','FEMENINO')
)

GRADO = (
	('INICIAL 3','INICIAL 3'),
	('INICIAL 4','INICIAL 4'),
	('INICIAL 5','INICIAL 5'),
	('1°','1°'),
	('2°','2°'),
	('3°','3°'),
	('4°','4°'),
	('5°','5°'),
	('6°','6°'),
	('7°','7°'),
	('8°','8°'),
	('9°','9°'),
	('10°','10°'),
	('11°','11°'),
	('12°','12°'),
	('13°','13°'),
	('14°','14°'),
)

TURNO = (
	('M','M'),
	('T','T')
)

ESTADO = (
	('ACTIVO','ACTIVO'),
	('INACTIVO','INACTIVO')
)

MOTIVO = (
	('INUBICADO','INUBICADO'),
	('RETIRADO','RETIRADO'),
	('FALLECIDO','FALLECIDO'),
	('DUPLICADO','DUPLICADO')
)

MUNICIPIO = (
	('LAMPA','LAMPA'),
	('PUNO','PUNO'),
	('PUTINA','PUTINA'),
	('LIMA','LIMA')
)

APADRINAMIENTO = (
	('APADRINADO','APADRINADO'),
	('NO APADRINADO','NO APADRINADO')
)

# Año de la diversificacion productiva y del fortalecimiento de la educacion

# Create your models here.
class General(models.Model):
	today = datetime.now()
	coordinacion = 'LA'
	year = today.year
	month = today.month
	codigo_inicial=coordinacion + today.strftime("%y") + today.strftime("%m")

	codigo_inicial = models.CharField(max_length=10, blank=True, default=codigo_inicial)
	codigo_de_menor = models.CharField(max_length=8, blank=True)
	nombres = models.CharField(max_length=100)
	apellidos = models.CharField(max_length=100)
	sexo = models.CharField(max_length=10, choices=SEXO)
	escuela = models.ForeignKey(Escuela, blank=True)
	escuela_anterior = models.CharField(max_length=50, blank=True)
	grado = models.CharField(max_length=20, choices=GRADO)
	seccion = models.CharField(max_length=20)
	turno = models.CharField(max_length=1, choices=TURNO, default='M')
	estado = models.CharField(max_length=10, choices=ESTADO, default='ACTIVO')
	motivo_estado = models.CharField(max_length=10, choices=MOTIVO, blank=True)
	notas = models.TextField(max_length=200, blank=True)
	salud = models.CharField(max_length=200, blank=True)
	duplicado = models.CharField(max_length=50, blank=True)
	direccion = models.CharField(max_length=200)
	barrio = models.CharField(max_length=100)
	poblacion = models.ForeignKey(Centro_poblado)
	municipio = models.CharField(max_length=50, choices=MUNICIPIO, default='LAMPA')
	padre = models.CharField(max_length=50)
	madre = models.CharField(max_length=50)
	celular = models.CharField(max_length=50, blank=True)
	dni = models.PositiveIntegerField(blank=True)
	numero_hermanos = models.PositiveSmallIntegerField()
	apadrinamiento = models.CharField(max_length=20, choices=APADRINAMIENTO, default='NO APADRINADO')
	padrino_codigo = models.CharField(max_length=8, blank=True)
	padrino_nombres = models.CharField(max_length=100, blank=True)
	padrino_apellidos = models.CharField(max_length=100, blank=True)
	padrino_sede = models.CharField(max_length=20, blank=True)
	observaciones = models.CharField(max_length=100, blank=True)

	def __unicode__(self):
		return self.codigo_inicial

	class Admin:
		pass