# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-29 10:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0002_auto_20170626_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]
