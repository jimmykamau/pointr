# Generated by Django 4.2.1 on 2023-05-18 11:49

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Points",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("points_list", models.TextField()),
                (
                    "closest_points",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
            ],
        ),
    ]
