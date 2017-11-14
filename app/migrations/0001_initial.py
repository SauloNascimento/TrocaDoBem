# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields
from django.conf import settings
import cloudinary.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CommonUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('published_at', models.DateTimeField(auto_now=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('cpf', models.CharField(max_length=100, default='Nao Informado')),
                ('street', models.CharField(max_length=100, default='Nao Informado')),
                ('number', models.CharField(max_length=10, default='Nao Informado')),
                ('district', models.CharField(max_length=100, default='Nao Informado')),
                ('cep', models.CharField(max_length=8, default='Nao informado')),
                ('complement', models.CharField(max_length=100, default='Nao Informado')),
                ('city', models.CharField(max_length=100, default='Nao Informado')),
                ('state', models.CharField(max_length=20, default='Nao Informado')),
                ('phone', models.CharField(max_length=30, default='Nao Informado')),
                ('user', models.ForeignKey(unique=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
            },
        ),
        migrations.CreateModel(
            name='ImagePost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('published_at', models.DateTimeField(auto_now=True)),
                ('image', cloudinary.models.CloudinaryField(verbose_name='image', max_length=255)),
                ('label', models.CharField(max_length=100, blank=True, null=True)),
                ('is_visible', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'ImagePost',
                'verbose_name_plural': 'ImagePosts',
            },
        ),
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('published_at', models.DateTimeField(auto_now=True)),
                ('photo', models.URLField(blank=True)),
                ('cnpj', models.CharField(max_length=100, default='Nao Informado')),
                ('cep', models.CharField(max_length=8, default='Nao Informado')),
                ('state', models.CharField(max_length=20, default='Nao Informado')),
                ('city', models.CharField(max_length=100, default='Nao Informado')),
                ('district', models.CharField(max_length=100, default='Nao Informado')),
                ('street', models.CharField(max_length=100, default='Nao Informado')),
                ('number', models.CharField(max_length=5, default='Nao Informado')),
                ('complement', models.CharField(max_length=200, blank=True)),
                ('description', models.CharField(max_length=100, blank=True)),
                ('phone', models.CharField(max_length=30, default='Nao Informado')),
                ('user', models.ForeignKey(unique=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Instituicao',
                'verbose_name_plural': 'Instituicoes',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('published_at', models.DateTimeField(auto_now=True)),
                ('description', models.CharField(max_length=300)),
                ('name_item', models.CharField(max_length=100)),
                ('photo', models.URLField()),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100, blank=True, null=True)),
                ('email', models.EmailField(max_length=254, blank=True, null=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Mensagem',
                'verbose_name_plural': 'Mensagens',
            },
        ),
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('published_at', models.DateTimeField(auto_now=True)),
                ('type', models.CharField(max_length=50, choices=[('Eletronicos', 'Eletronicos'), ('Calcados', 'Calcados'), ('Pereciveis', 'Pereciveis')])),
                ('item', models.ForeignKey(unique=True, to='app.Item')),
            ],
            options={
                'verbose_name': 'Objeto',
                'verbose_name_plural': 'Objetos',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('published_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=150)),
                ('text', ckeditor.fields.RichTextField()),
                ('is_visible', models.BooleanField(default=True)),
                ('slug', models.SlugField(unique=True)),
                ('author', models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('published_at', models.DateTimeField(auto_now=True)),
                ('item', models.ForeignKey(unique=True, to='app.Item')),
            ],
            options={
                'verbose_name': 'Servico',
                'verbose_name_plural': 'Servicos',
            },
        ),
        migrations.AddField(
            model_name='imagepost',
            name='model',
            field=models.ForeignKey(blank=True, null=True, to='app.Post'),
        ),
    ]
