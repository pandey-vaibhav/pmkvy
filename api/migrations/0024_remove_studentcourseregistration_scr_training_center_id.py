# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-24 10:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_auto_20170324_1011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentcourseregistration',
            name='scr_training_center_id',
        ),
    ]