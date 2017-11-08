# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20171106_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='instituicao',
            name='senha',
            field=models.CharField(max_length=20, default='12345678'),
        ),
    ]
