# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='instituicao',
            name='bairro',
            field=models.CharField(max_length=100, default='Nao Informado'),
        ),
        migrations.AddField(
            model_name='instituicao',
            name='cep',
            field=models.CharField(max_length=8, default='Nao Informado'),
        ),
        migrations.AddField(
            model_name='instituicao',
            name='cidade',
            field=models.CharField(max_length=100, default='Nao Informado'),
        ),
        migrations.AddField(
            model_name='instituicao',
            name='complemento',
            field=models.CharField(max_length=200, default='Nao Informado'),
        ),
        migrations.AddField(
            model_name='instituicao',
            name='descricao',
            field=models.CharField(max_length=100, default='Nao Informado'),
        ),
        migrations.AddField(
            model_name='instituicao',
            name='email',
            field=models.EmailField(max_length=254, blank=True),
        ),
        migrations.AddField(
            model_name='instituicao',
            name='estado',
            field=models.CharField(max_length=20, default='Nao Informado'),
        ),
        migrations.AddField(
            model_name='instituicao',
            name='name',
            field=models.CharField(max_length=100, default='Nao Informado'),
        ),
        migrations.AddField(
            model_name='instituicao',
            name='numero',
            field=models.CharField(max_length=5, default='Nao Informado'),
        ),
        migrations.AddField(
            model_name='instituicao',
            name='rua',
            field=models.CharField(max_length=100, default='Nao Informado'),
        ),
        migrations.AddField(
            model_name='instituicao',
            name='telefone',
            field=models.CharField(max_length=30, default='Nao Informado'),
        ),
        migrations.AlterField(
            model_name='instituicao',
            name='cnpj',
            field=models.CharField(max_length=100, default='Nao Informado'),
        ),
    ]
