# Generated by Django 4.2.6 on 2023-12-03 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Services",
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
                ("title", models.CharField(max_length=200, verbose_name="Titulo")),
                (
                    "subtitle",
                    models.CharField(max_length=200, verbose_name="Subtitulo"),
                ),
                ("content", models.TextField(verbose_name="Contenido")),
                (
                    "image",
                    models.ImageField(upload_to="services", verbose_name="Imagen"),
                ),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Fecha creacion"
                    ),
                ),
                (
                    "updated",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Fecha de edicion"
                    ),
                ),
            ],
            options={
                "verbose_name": "servicio",
                "verbose_name_plural": "servicios",
                "ordering": ["-created"],
            },
        ),
    ]
