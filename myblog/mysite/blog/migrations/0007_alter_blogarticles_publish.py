# Generated by Django 4.2.5 on 2023-09-27 12:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0006_alter_blogarticles_publish"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogarticles",
            name="publish",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 9, 27, 12, 38, 20, 128393, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
