# Generated by Django 4.2.5 on 2023-10-05 12:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0014_alter_blogarticles_publish"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogarticles",
            name="publish",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 10, 5, 12, 37, 25, 898631, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
