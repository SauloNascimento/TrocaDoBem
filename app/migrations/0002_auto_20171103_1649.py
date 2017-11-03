# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Message',
            new_name='Mensagem',
        ),
        migrations.AlterModelOptions(
            name='mensagem',
            options={'verbose_name': 'Mensagem', 'verbose_name_plural': 'Mensagens'},
        ),
    ]
