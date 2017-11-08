# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_instituicao_senha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instituicao',
            name='photo',
            field=models.URLField(blank=True),
        ),
    ]
