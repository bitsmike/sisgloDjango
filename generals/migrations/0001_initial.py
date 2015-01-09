# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('escuelas', '0001_initial'),
        ('centros_poblados', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='General',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo_inicial', models.CharField(max_length=10, blank=True)),
                ('padrino_codigo', models.CharField(max_length=8, blank=True)),
                ('padrino_nombres', models.CharField(max_length=100, blank=True)),
                ('padrino_apellidos', models.CharField(max_length=100, blank=True)),
                ('padrino_sede', models.CharField(max_length=20, blank=True)),
                ('codigo_de_menor', models.CharField(max_length=8, blank=True)),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('sexo', models.CharField(max_length=10, choices=[(b'M', b'MASCULINO'), (b'F', b'FEMENINO')])),
                ('escuela_anterior', models.CharField(max_length=50, blank=True)),
                ('grado', models.CharField(max_length=20, choices=[(b'INICIAL 3', b'INICIAL 3'), (b'INICIAL 4', b'INICIAL 4'), (b'INICIAL 5', b'INICIAL 5'), (b'1\xc2\xb0', b'1\xc2\xb0'), (b'2\xc2\xb0', b'2\xc2\xb0'), (b'3\xc2\xb0', b'3\xc2\xb0'), (b'4\xc2\xb0', b'4\xc2\xb0'), (b'5\xc2\xb0', b'5\xc2\xb0'), (b'6\xc2\xb0', b'6\xc2\xb0'), (b'7\xc2\xb0', b'7\xc2\xb0'), (b'8\xc2\xb0', b'8\xc2\xb0'), (b'9\xc2\xb0', b'9\xc2\xb0'), (b'10\xc2\xb0', b'10\xc2\xb0'), (b'11\xc2\xb0', b'11\xc2\xb0'), (b'12\xc2\xb0', b'12\xc2\xb0'), (b'13\xc2\xb0', b'13\xc2\xb0'), (b'14\xc2\xb0', b'14\xc2\xb0')])),
                ('seccion', models.CharField(max_length=20)),
                ('turno', models.CharField(max_length=1)),
                ('estado', models.CharField(max_length=10, choices=[(b'ACTIVO', b'ACTIVO'), (b'INACTIVO', b'ACTIVO')])),
                ('motivo_estado', models.CharField(blank=True, max_length=10, choices=[(b'INUBICADO', b'INUBICADO'), (b'RETIRADO', b'RETIRADO'), (b'FALLECIDO', b'FALLECIDO'), (b'DUPLICADO', b'DUPLICADO')])),
                ('notas', models.TextField(max_length=200, blank=True)),
                ('salud', models.TextField(max_length=200, blank=True)),
                ('duplicado', models.TextField(max_length=50, blank=True)),
                ('direccion', models.TextField(max_length=200)),
                ('barrio', models.TextField(max_length=100)),
                ('municipio', models.TextField(max_length=50, choices=[(b'LAMPA', b'LAMPA'), (b'PUNO', b'PUNO'), (b'PUTINA', b'PUTINA'), (b'LIMA', b'LIMA')])),
                ('padre', models.TextField(max_length=50)),
                ('madre', models.TextField(max_length=50)),
                ('celular', models.TextField(max_length=50, blank=True)),
                ('dni', models.PositiveIntegerField(blank=True)),
                ('numero_hermanos', models.PositiveSmallIntegerField()),
                ('apadrinamiento', models.TextField(default=b'NO APADRINADO', max_length=20, choices=[(b'APADRINADO', b'APADRINADO'), (b'NO APADRINADO', b'NO APADRINADO')])),
                ('observaciones', models.TextField(max_length=100, blank=True)),
                ('escuela', models.ForeignKey(to='escuelas.Escuela')),
                ('poblacion', models.ForeignKey(to='centros_poblados.Centro_poblado')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
