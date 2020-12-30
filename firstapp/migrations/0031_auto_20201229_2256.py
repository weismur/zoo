# Generated by Django 3.1.4 on 2020-12-29 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0030_auto_20201229_2231'),
    ]

    operations = [
        migrations.AddField(
            model_name='reptile',
            name='normal_temperature',
            field=models.IntegerField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='animal',
            name='area_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.habitat_area'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='ration_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.feeding_ration'),
        ),
        migrations.AlterField(
            model_name='bird',
            name='animal_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.animal'),
        ),
        migrations.AlterField(
            model_name='reptile',
            name='animal_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.animal'),
        ),
    ]
