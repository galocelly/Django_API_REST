# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('escuela', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100, blank=True)),
                ('apellido', models.CharField(max_length=100, blank=True)),
                ('cedula', models.CharField(max_length=11, blank=True)),
                ('ciudad', models.CharField(max_length=100, blank=True)),
                ('provincia', models.CharField(max_length=100, blank=True)),
            ],
            options={
                'ordering': ('apellido',),
            },
        ),
    ]
