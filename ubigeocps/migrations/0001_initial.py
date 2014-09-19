# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cenpobs', '__first__'),
        ('municipios', '0001_initial'),
        ('distritos', '__first__'),
        ('provincias', '__first__'),
        ('departamentos', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ubigeocp',
            fields=[
                ('Codigo_Ubigeocp', models.CharField(max_length=12, unique=True, serialize=False, primary_key=True)),
                ('pais', models.CharField(default=b'PERU', max_length=20)),
                ('Centro_poblado', models.ForeignKey(to='cenpobs.Cenpob')),
                ('departamento', models.ForeignKey(to='departamentos.Departamento')),
                ('distrito', models.ForeignKey(to='distritos.Distrito')),
                ('municipio', models.ForeignKey(to='municipios.Municipio')),
                ('provincia', models.ForeignKey(to='provincias.Provincia')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
