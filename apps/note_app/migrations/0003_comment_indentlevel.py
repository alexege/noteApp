# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2019-12-07 01:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note_app', '0002_auto_20191121_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='indentLevel',
            field=models.IntegerField(default=0),
        ),
    ]
