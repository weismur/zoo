# Generated by Django 3.1.2 on 2020-12-29 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0020_auto_20201229_1915'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animal',
            old_name='area',
            new_name='area_id',
        ),
        migrations.RenameField(
            model_name='animal',
            old_name='ration',
            new_name='ration_id',
        ),
    ]