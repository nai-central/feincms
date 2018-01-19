# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import feincms.extensions
import feincms.translations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('slug', models.SlugField(max_length=150, verbose_name='slug')),
                ('parent', models.ForeignKey(related_name='children', verbose_name='parent', blank=True, to='medialibrary.Category', null=True, on_delete=models.CASCADE)),
            ],
            options={
                'ordering': ['parent__title', 'title'],
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='MediaFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.FileField(upload_to='medialibrary/%Y/%m/', max_length=255, verbose_name='file')),
                ('type', models.CharField(verbose_name='file type', max_length=12, editable=False, choices=[('image', 'Image'), ('video', 'Video'), ('audio', 'Audio'), ('pdf', 'PDF document'), ('swf', 'Flash'), ('txt', 'Text'), ('rtf', 'Rich Text'), ('zip', 'Zip archive'), ('doc', 'Microsoft Word'), ('xls', 'Microsoft Excel'), ('ppt', 'Microsoft PowerPoint'), ('other', 'Binary')])),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('copyright', models.CharField(max_length=200, verbose_name='copyright', blank=True)),
                ('file_size', models.IntegerField(verbose_name='file size', null=True, editable=False, blank=True)),
                ('categories', models.ManyToManyField(to='medialibrary.Category', verbose_name='categories', blank=True)),
            ],
            bases=(models.Model, feincms.extensions.ExtensionsMixin, feincms.translations.TranslatedObjectMixin),
        ),
        migrations.CreateModel(
            name='MediaFileTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language_code', models.CharField(default=b'en', verbose_name='language', max_length=10, editable=False, choices=[(b'en', b'English')])),
                ('caption', models.CharField(max_length=200, verbose_name='caption')),
                ('description', models.TextField(verbose_name='description', blank=True)),
                ('parent', models.ForeignKey(related_name='translations', to='medialibrary.MediaFile', on_delete=models.CASCADE)),
            ],
            options={
                'verbose_name': 'media file translation',
                'verbose_name_plural': 'media file translations',
            },
        ),
        migrations.AlterUniqueTogether(
            name='mediafiletranslation',
            unique_together=set([('parent', 'language_code')]),
        ),
    ]
