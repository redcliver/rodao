# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-03 08:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordem', '0003_auto_20180402_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordens',
            name='estado',
            field=models.CharField(choices=[('1', 'Em Aberto'), ('2', 'Finalizada')], max_length=1),
        ),
    ]
