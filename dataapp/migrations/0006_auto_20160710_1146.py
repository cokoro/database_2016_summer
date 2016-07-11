# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-10 03:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dataapp', '0005_auto_20160709_2337'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataapp.CourseInfo')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataapp.TeacherInfo')),
            ],
        ),
        migrations.AddField(
            model_name='studentcourse',
            name='teacher_id',
            field=models.ForeignKey(default=2016, on_delete=django.db.models.deletion.CASCADE, to='dataapp.TeacherInfo'),
        ),
    ]