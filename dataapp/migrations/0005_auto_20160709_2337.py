# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-09 15:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataapp', '0004_auto_20160709_2311'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentinfo',
            old_name='stu_id',
            new_name='student_id',
        ),
        migrations.RenameField(
            model_name='studentinfo',
            old_name='stu_name',
            new_name='student_name',
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='class_id',
            field=models.IntegerField(),
        ),
    ]
