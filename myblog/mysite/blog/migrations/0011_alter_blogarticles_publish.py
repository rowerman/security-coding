# Generated by Django 4.2.5 on 2023-10-04 07:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0010_alter_blogarticles_publish"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogarticles",
            name="publish",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 10, 4, 7, 17, 28, 482624, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
