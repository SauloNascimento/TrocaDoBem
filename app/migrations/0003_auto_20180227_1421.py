# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-27 17:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_institutesingup'),
    ]

    operations = [
        migrations.RenameField(
            model_name='institutesingup',
            old_name='login',
            new_name='username',
        ),
    ]