# Generated by Django 3.1.4 on 2020-12-21 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_auto_20201221_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card_db',
            name='accuracy_date',
            field=models.BooleanField(),
        ),
    ]
