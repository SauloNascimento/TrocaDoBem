# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20171120_2229'),
    ]

    operations = [
        migrations.AddField(
            model_name='commonuser',
            name='anonymous',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='object',
            name='type',
            field=models.CharField(max_length=50, choices=[('Eletronicos', 'Eletronicos'), ('Vestimentas', 'Vestimentas'), ('Alimentos', 'Alimentos'), ('Higiene', 'Higiene'), ('Mobilia', 'Mobilia'), ('Brinquedos', 'Brinquedos'), ('Papelaria', 'Papelaria'), ('Outros', 'Outros')]),
        ),
    ]
