# Generated by Django 4.2.5 on 2023-10-06 03:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0016_alter_blogarticles_publish"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogarticles",
            name="publish",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 10, 6, 3, 17, 33, 659646, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
