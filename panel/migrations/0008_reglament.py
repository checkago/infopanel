# Generated by Django 4.2.9 on 2024-03-15 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("panel", "0007_pushkincard"),
    ]

    operations = [
        migrations.CreateModel(
            name="Reglament",
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
                ("name", models.CharField(max_length=150, verbose_name="Наименование")),
                ("description", models.TextField(verbose_name="Описание")),
            ],
            options={
                "verbose_name": "Регламент",
                "verbose_name_plural": "Регламенты",
            },
        ),
    ]
