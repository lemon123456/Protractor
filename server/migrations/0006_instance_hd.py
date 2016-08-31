# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-13 01:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0005_auto_20160712_2353'),
    ]

    operations = [
        migrations.AddField(
            model_name='instance',
            name='hd',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='server.HardDisk'),
            preserve_default=False,
        ),
    ]