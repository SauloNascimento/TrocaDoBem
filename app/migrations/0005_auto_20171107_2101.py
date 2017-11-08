# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20171106_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='login',
            field=models.CharField(max_length=15, default='Nao Informado'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='senha',
            field=models.CharField(max_length=25, default='Nao Informado'),
        ),
    ]
