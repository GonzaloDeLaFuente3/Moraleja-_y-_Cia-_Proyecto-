# Generated by Django 4.2.1 on 2023-05-19 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seccion', '0002_alter_seccion_descripcion_alter_seccion_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seccion',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='media/img'),
        ),
    ]
