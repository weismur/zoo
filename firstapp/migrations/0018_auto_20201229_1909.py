# Generated by Django 3.1.2 on 2020-12-29 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0017_auto_20201229_1907'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='area',
        ),
        migrations.RemoveField(
            model_name='animal',
            name='ration',
        ),
    ]
