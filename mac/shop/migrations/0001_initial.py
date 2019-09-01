# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-06 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('decs', models.CharField(max_length=300)),
                ('pub_date', models.DateField()),
            ],
        ),
    ]
