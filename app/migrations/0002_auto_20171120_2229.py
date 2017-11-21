# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commonuser',
            name='cep',
            field=models.CharField(max_length=15, default='Nao Informado'),
        ),
        migrations.AlterField(
            model_name='institute',
            name='cep',
            field=models.CharField(max_length=15, default='Nao Informado'),
        ),
    ]
