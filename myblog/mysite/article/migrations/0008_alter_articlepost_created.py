# Generated by Django 4.2.5 on 2023-10-05 12:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("article", "0007_alter_articlepost_created"),
    ]

    operations = [
        migrations.AlterField(
            model_name="articlepost",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 10, 5, 12, 37, 25, 916553, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]