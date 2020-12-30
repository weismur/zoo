# Generated by Django 3.1.4 on 2020-12-21 15:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_author_db_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='card_db',
            name='accuracy_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='card_db',
            name='create_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='exhibition_db',
            name='finish_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='exhibition_db',
            name='start_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
