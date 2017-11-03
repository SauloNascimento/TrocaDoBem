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
            name='Instituicao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('published_at', models.DateTimeField(auto_now=True)),
                ('photo', models.URLField()),
                ('cnpj', models.CharField(max_length=100)),
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
                ('descricao', models.CharField(max_length=300)),
                ('nome_item', models.CharField(max_length=100)),
                ('photo', models.URLField()),
                ('dono', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Mensagem',
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
            name='Objeto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('published_at', models.DateTimeField(auto_now=True)),
                ('tipo', models.CharField(max_length=50, choices=[('Eletronicos', 'Eletronicos'), ('Calcados', 'Calcados'), ('Pereciveis', 'Pereciveis')])),
                ('item', models.ForeignKey(unique=True, to='app.Item')),
            ],
            options={
                'abstract': False,
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
            name='Servico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('published_at', models.DateTimeField(auto_now=True)),
                ('item', models.ForeignKey(unique=True, to='app.Item')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('published_at', models.DateTimeField(auto_now=True)),
                ('photo', cloudinary.models.CloudinaryField(max_length=255)),
                ('user', models.ForeignKey(unique=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='imagepost',
            name='model',
            field=models.ForeignKey(blank=True, null=True, to='app.Post'),
        ),
    ]
