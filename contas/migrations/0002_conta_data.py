# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-03 08:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='conta',
            name='data',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
