# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Escuela',
            fields=[
                ('codmod', models.CharField(max_length=7, serialize=False, primary_key=True)),
                ('situacion', models.CharField(max_length=8, choices=[(b'ACTIVO', b'ACTIVO'), (b'INACTIVO', b'INACTIVO')])),
                ('ruta', models.CharField(max_length=8, choices=[(b'RUTA 01', b'RUTA 01'), (b'RUTA 02', b'RUTA 02'), (b'RUTA 03', b'RUTA 03'), (b'RUTA 04', b'RUTA 04'), (b'RUTA 05', b'RUTA 05'), (b'RUTA 06', b'RUTA 06'), (b'RUTA 07', b'RUTA 07'), (b'RUTA 08', b'RUTA 08'), (b'RUTA 09', b'RUTA 09'), (b'RUTA 10', b'RUTA 10'), (b'RUTA 11', b'RUTA 11'), (b'RUTA 12', b'RUTA 12'), (b'RUTA 13', b'RUTA 13'), (b'RUTA 14', b'RUTA 14'), (b'RUTA 15', b'RUTA 15'), (b'RUTA 16', b'RUTA 16'), (b'RUTA 17', b'RUTA 17'), (b'OTRO', b'OTRO')])),
                ('numero', models.CharField(max_length=5, blank=True)),
                ('prenombre', models.CharField(max_length=160, choices=[(b'PRONOEI', b'PRONOEI'), (b'INICIAL', b'INICIAL'), (b'IEP', b'IEP'), (b'IEP-NO ESCOLARIZADO', b'IEP-NO ESCOLARIZADO'), (b'IES', b'IES'), (b'IES-NO ESCOLARIZADO', b'IES-NO ESCOLARIZADO'), (b'CEBA', b'CEBA'), (b'IST', b'IST'), (b'ISPT', b'ISPT'), (b'ESFA', b'ESFA'), (b'CETPRO', b'CETPRO'), (b'CEO', b'CEO'), (b'CEO-CETPRO', b'CEO-CETPRO'), (b'CEO-ARTESANAL', b'CEO-ARTESANAL')])),
                ('nombre', models.CharField(max_length=200)),
                ('escuela_ghp', models.CharField(max_length=160, choices=[(b'SI', b'SI'), (b'NO', b'NO')])),
                ('nivel', models.CharField(max_length=100, choices=[(b'PRIMARIA', b'PRIMARIA'), (b'INICIAL', b'INICIAL'), (b'SECUNDARIA', b'SECUNDARIA'), (b'SUPERIOR', b'SUPERIOR'), (b'CETPRO', b'CETPRO'), (b'OTRO', b'OTRO')])),
                ('codigo_ghp', models.CharField(max_length=5)),
                ('direccion', models.CharField(max_length=200)),
                ('poblacion', models.CharField(max_length=50)),
                ('distrito', models.CharField(max_length=50)),
                ('provincia', models.CharField(max_length=50)),
                ('departamento', models.CharField(max_length=50)),
                ('ugel', models.CharField(max_length=100, blank=True)),
                ('fecha_de_registro', models.DateField()),
                ('msnm', models.PositiveSmallIntegerField()),
                ('director', models.CharField(max_length=200, blank=True)),
                ('dni', models.CharField(max_length=8, blank=True)),
                ('usuario_siagie', models.CharField(max_length=50, blank=True)),
                ('password_siagie', models.CharField(max_length=50, blank=True)),
                ('celular', models.CharField(max_length=200, blank=True)),
                ('nro_computadoras', models.PositiveSmallIntegerField(blank=True)),
                ('nro_laptops', models.PositiveSmallIntegerField(blank=True)),
                ('con_qaliwarma', models.CharField(blank=True, max_length=200, choices=[(b'SI', b'SI'), (b'NO', b'NO')])),
                ('quintil_de_probreza', models.CharField(max_length=15, choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'INDETERMINADO', b'INDETERMINADO')])),
                ('num_docentes', models.PositiveSmallIntegerField(blank=True)),
                ('num_secciones', models.PositiveSmallIntegerField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
