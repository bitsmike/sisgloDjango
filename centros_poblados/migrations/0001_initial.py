# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Centro_poblado',
            fields=[
                ('codigo_cenpob', models.CharField(max_length=6, serialize=False, primary_key=True)),
                ('nombre_cenpob', models.CharField(max_length=100)),
                ('con_ie', models.CharField(max_length=1)),
                ('nivel_ie', models.CharField(max_length=9, blank=True)),
                ('fuente_g', models.CharField(max_length=45)),
                ('msnm', models.CharField(max_length=4)),
                ('XGD', models.CharField(max_length=20)),
                ('YGD', models.CharField(max_length=20)),
                ('pais', models.CharField(default=b'PERU', max_length=20)),
                ('cp_dis_prov_dep', models.CharField(max_length=200)),
                ('dep_prov_dis_cp', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('cod_departamento', models.CharField(max_length=2, serialize=False, primary_key=True)),
                ('name_departamento', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Distrito',
            fields=[
                ('cod_distrito', models.CharField(max_length=6, serialize=False, primary_key=True)),
                ('name_distrito', models.CharField(max_length=100)),
                ('departamento', models.ForeignKey(to='centros_poblados.Departamento')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('cod_provincia', models.CharField(max_length=4, serialize=False, primary_key=True)),
                ('name_provincia', models.CharField(max_length=100)),
                ('departamento', models.ForeignKey(to='centros_poblados.Departamento')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='distrito',
            name='provincia',
            field=models.ForeignKey(to='centros_poblados.Provincia'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='centro_poblado',
            name='departamento',
            field=models.ForeignKey(to='centros_poblados.Departamento'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='centro_poblado',
            name='distrito',
            field=models.ForeignKey(to='centros_poblados.Distrito'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='centro_poblado',
            name='provincia',
            field=models.ForeignKey(to='centros_poblados.Provincia'),
            preserve_default=True,
        ),
    ]
