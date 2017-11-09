# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20171108_2238'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doacao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('published_at', models.DateTimeField(auto_now=True)),
                ('data_doacao', models.DateField(blank=True, null=True)),
                ('id_instituicao', models.ForeignKey(unique=True, to='app.Instituicao')),
                ('id_usuario', models.ForeignKey(unique=True, to='app.Usuario')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
