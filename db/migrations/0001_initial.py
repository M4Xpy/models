# Generated by Django 5.0.1 on 2024-01-08 12:06

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Car",
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
                ("brand", models.CharField(max_length=255)),
                ("horsepower", models.IntegerField()),
                ("creation_date", models.DateField()),
                ("description", models.TextField()),
            ],
        ),
    ]
