# Generated by Django 3.1.3 on 2024-10-22 14:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0017_merge_20210127_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam_model',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 22, 19, 53, 51, 774319)),
        ),
        migrations.AlterField(
            model_name='exam_model',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 22, 19, 53, 51, 774319)),
        ),
    ]
