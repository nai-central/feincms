# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medialibrary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediafiletranslation',
            name='caption',
            field=models.CharField(max_length=512, verbose_name='caption'),
        ),
    ]
