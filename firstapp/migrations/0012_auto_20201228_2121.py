# Generated by Django 3.1.2 on 2020-12-28 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0011_remove_bird_code_of_wintering_place'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reptile',
            name='hibernation_period',
            field=models.CharField(max_length=45),
        ),
    ]
