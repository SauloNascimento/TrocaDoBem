# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_commonuser_anonymous'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commonuser',
            name='anonymous',
            field=models.BooleanField(default=False),
        ),
    ]
