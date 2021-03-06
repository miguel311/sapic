# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-22 20:16
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import explicacion_situacional.modelsExplicacion.modelsExplicacionesSituacional


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organizaciones', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Caracterizacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caracterizacion', models.CharField(max_length=128, unique=True, verbose_name='Caracterización')),
                ('descripcion', models.TextField()),
            ],
            options={
                'verbose_name': 'Caracterización',
                'verbose_name_plural': 'Características',
                'ordering': ('caracterizacion',),
            },
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_consulta', models.CharField(max_length=128, unique=True)),
                ('activa', models.BooleanField(default=True)),
                ('fk_caracterizacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='explicacion_situacional.Caracterizacion')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Consulta',
                'verbose_name_plural': 'Consultas',
                'ordering': ('nombre_consulta',),
            },
        ),
        migrations.CreateModel(
            name='ExplicacionSituacional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coordenadas', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
                ('map_cartografico', models.FileField(upload_to=explicacion_situacional.modelsExplicacion.modelsExplicacionesSituacional.ExplicacionSituacional.get_upload_to)),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('fk_organizacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizaciones.OrganizacionSocial')),
            ],
            options={
                'verbose_name': 'Explicacion situacional',
                'verbose_name_plural': 'Explicaciones Situacionales',
                'ordering': ('fk_organizacion',),
            },
        ),
        migrations.CreateModel(
            name='ExplicSitConsulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('fk_consulta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='explicacion_situacional.Consulta')),
                ('fk_explicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='explicacion_situacional.ExplicacionSituacional')),
            ],
            options={
                'verbose_name': 'Asignacion de Consulta a una explicacion situacional',
                'verbose_name_plural': 'Asignaciones de consultas a las explicaciones situacionales',
                'ordering': ('fk_consulta',),
            },
        ),
        migrations.CreateModel(
            name='Opcion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto_opcion', models.TextField()),
            ],
            options={
                'verbose_name': 'Opcion',
                'verbose_name_plural': 'Opciones',
                'ordering': ('pregunta',),
            },
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto_pregunta', models.TextField()),
                ('consulta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='explicacion_situacional.Consulta')),
            ],
            options={
                'verbose_name': 'pregunta',
                'verbose_name_plural': 'Preguntas',
                'ordering': ('consulta',),
            },
        ),
        migrations.CreateModel(
            name='RespuestaAbierta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto_respuesta', models.TextField()),
                ('es_justificacion', models.BooleanField(default=False)),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='explicacion_situacional.Pregunta')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RespuestaOpciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opcion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='explicacion_situacional.Opcion')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RespuestaSino',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respuesta', models.BooleanField()),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='explicacion_situacional.Pregunta')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RespuestaUbicacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coordenadas', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='explicacion_situacional.Pregunta')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TipoPregunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Tipo Pregunta',
                'verbose_name_plural': 'Tipos de Preguntas',
                'ordering': ('tipo',),
            },
        ),
        migrations.AddField(
            model_name='pregunta',
            name='tipo_pregunta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='explicacion_situacional.TipoPregunta'),
        ),
        migrations.AddField(
            model_name='opcion',
            name='pregunta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='explicacion_situacional.Pregunta'),
        ),
    ]
