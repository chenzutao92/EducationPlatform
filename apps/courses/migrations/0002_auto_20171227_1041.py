# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-27 10:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_auto_20171227_0836'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='courseresource',
            options={'verbose_name': '课程资源', 'verbose_name_plural': '课程资源'},
        ),
        migrations.AddField(
            model_name='course',
            name='course_org',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.CourseOrg', verbose_name='课程机构'),
        ),
        migrations.AlterField(
            model_name='course',
            name='degree',
            field=models.CharField(choices=[('cj', '初级'), ('zj', '中级'), ('gj', '高级')], max_length=2, verbose_name='难度'),
        ),
    ]