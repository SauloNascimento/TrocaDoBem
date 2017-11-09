# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cloudinary.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_merge'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='endereco',
            new_name='rua',
        ),
        migrations.RemoveField(
            model_name='instituicao',
            name='user',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='user',
        ),
        migrations.AlterField(
            model_name='instituicao',
            name='complemento',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='instituicao',
            name='descricao',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='photo',
            field=cloudinary.models.CloudinaryField(max_length=255, blank=True),
        ),
    ]
