# Generated by Django 4.1.7 on 2023-06-30 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("seccion", "0009_alter_seccion_options_remove_seccion_descripcion_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historia",
            name="imagen",
            field=models.ImageField(blank=True, upload_to="img"),
        ),
        migrations.AlterField(
            model_name="nosotros",
            name="imagen",
            field=models.ImageField(blank=True, upload_to="img"),
        ),
    ]
