# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-13 02:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0002_host_account'),
        ('appconf', '0004_auto_20190313_1047'),
        ('accounts', '0002_auto_20180827_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='rolelist',
            name='delivery',
            field=models.ManyToManyField(blank=True, to='appconf.Project'),
        ),
        migrations.AddField(
            model_name='rolelist',
            name='webssh',
            field=models.ManyToManyField(blank=True, to='cmdb.HostGroup'),
        ),
    ]
