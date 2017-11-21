# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commonuser',
            name='address',
        ),
        migrations.RemoveField(
            model_name='commonuser',
            name='cep',
        ),
        migrations.RemoveField(
            model_name='commonuser',
            name='city',
        ),
        migrations.RemoveField(
            model_name='commonuser',
            name='complement',
        ),
        migrations.RemoveField(
            model_name='commonuser',
            name='district',
        ),
        migrations.RemoveField(
            model_name='commonuser',
            name='number',
        ),
        migrations.RemoveField(
            model_name='commonuser',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='commonuser',
            name='state',
        ),
    ]
