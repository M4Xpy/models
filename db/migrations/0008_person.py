# Generated by Django 5.0.1 on 2024-01-08 17:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("db", "0007_alter_company_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="Person",
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
                ("name", models.CharField(max_length=63)),
                ("age", models.IntegerField()),
            ],
        ),
    ]