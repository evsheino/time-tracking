# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetrack', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workentry',
            name='time_from',
        ),
        migrations.RemoveField(
            model_name='workentry',
            name='time_to',
        ),
        migrations.AddField(
            model_name='workentry',
            name='hours',
            field=models.FloatField(default=0, verbose_name='tunnit'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='workentry',
            name='comment',
            field=models.TextField(verbose_name='kommentti'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='workentry',
            name='date',
            field=models.DateField(verbose_name='päivämäärä'),
            preserve_default=True,
        ),
    ]
