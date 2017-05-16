# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-16 02:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20160815_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.CharField(choices=[('almargen', 'Al Margen'), ('cyt', 'Ciencia y Tecnología'), ('cnv', 'Como Nos Ven'), ('econoinf', 'Econoinformal'), ('editorial', 'Editorial'), ('elbobo', 'El Bobo'), ('elintruso', 'El Intruso'), ('elw', 'El W'), ('endebate', 'En Deb(A)te'), ('exogeno', 'Exógeno'), ('opinion', 'Opinión'), ('personajes', 'Personajes')], default='', max_length=100),
        ),
    ]