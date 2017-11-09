# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20171106_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='bairro',
            field=models.CharField(max_length=100, default='Nao Informado'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='cep',
            field=models.CharField(max_length=8, default='Nao informado'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='cidade',
            field=models.CharField(max_length=100, default='Nao Informado'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='complemento',
            field=models.CharField(max_length=100, default='Nao Informado'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='cpf',
            field=models.CharField(max_length=100, default='Nao Informado'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='dataNascimento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='email',
            field=models.EmailField(max_length=254, blank=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='endereco',
            field=models.CharField(max_length=100, default='Nao Informado'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='estado',
            field=models.CharField(max_length=20, default='Nao Informado'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='nome',
            field=models.CharField(max_length=150, default='Nao Informado'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='numero',
            field=models.CharField(max_length=10, default='Nao Informado'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='telefone',
            field=models.CharField(max_length=30, default='Nao Informado'),
        ),
    ]
