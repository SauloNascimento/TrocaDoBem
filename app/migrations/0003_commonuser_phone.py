# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20171120_2208'),
    ]

    operations = [
        migrations.AddField(
            model_name='commonuser',
            name='phone',
            field=models.CharField(max_length=30, default='Nao Informado'),
        ),
    ]
