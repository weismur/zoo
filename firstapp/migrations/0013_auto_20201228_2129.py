# Generated by Django 3.1.2 on 2020-12-28 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0012_auto_20201228_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reptile',
            name='hibernation_period',
            field=models.CharField(max_length=45, null=True),
        ),
    ]
