# Generated by Django 3.1.4 on 2021-01-03 00:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0033_auto_20201229_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='area_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='firstapp.habitat_area'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='caretaker_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='caretaker_id', to='firstapp.user'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='ration_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='firstapp.feeding_ration'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='veterenarian_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='veterenarian_id', to='firstapp.user'),
        ),
        migrations.AlterField(
            model_name='bird',
            name='animal_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='firstapp.animal'),
        ),
        migrations.AlterField(
            model_name='reptile',
            name='animal_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='firstapp.animal'),
        ),
    ]