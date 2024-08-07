# Generated by Django 5.0.4 on 2024-06-20 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("survivorcompass", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Curso",
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
                ("nombre", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Estudiante",
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
                ("nombre", models.CharField(max_length=200, null=True)),
                ("apellidos", models.CharField(max_length=200, null=True)),
                ("fecha_nacimiento", models.DateTimeField(null=True)),
            ],
        ),
        migrations.DeleteModel(
            name="Estudiantes",
        ),
    ]
