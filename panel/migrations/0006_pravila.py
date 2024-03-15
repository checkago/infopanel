# Generated by Django 4.2.9 on 2024-03-15 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("panel", "0005_section_active"),
    ]

    operations = [
        migrations.CreateModel(
            name="Pravila",
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
                ("name", models.CharField(max_length=100, verbose_name="Наименование")),
                ("description", models.TextField(verbose_name="Текст")),
            ],
            options={
                "verbose_name": "Правила",
                "verbose_name_plural": "Правила",
            },
        ),
    ]
