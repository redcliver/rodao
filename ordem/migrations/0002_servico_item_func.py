# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-02 21:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0001_initial'),
        ('ordem', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servico_item',
            name='func',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='funcionario.funcionario'),
            preserve_default=False,
        ),
    ]
