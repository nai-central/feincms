# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medialibrary', '0002_auto_20160302_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediafiletranslation',
            name='caption',
            field=models.CharField(max_length=1024, verbose_name='caption'),
        ),
    ]
