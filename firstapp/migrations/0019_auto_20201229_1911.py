# Generated by Django 3.1.2 on 2020-12-29 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0018_auto_20201229_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='area',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='firstapp.habitat_area'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='animal',
            name='ration',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='firstapp.feeding_ration'),
            preserve_default=False,
        ),
    ]
