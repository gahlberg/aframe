# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2018-06-14 18:53
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('screens', '0005_screenwidgetconfig'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screen',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
