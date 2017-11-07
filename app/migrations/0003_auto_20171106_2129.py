# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20171106_2112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='bairro',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='cep',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='cidade',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='complemento',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='cpf',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='dataNascimento',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='email',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='endereco',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='nome',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='numero',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='telefone',
        ),
    ]
