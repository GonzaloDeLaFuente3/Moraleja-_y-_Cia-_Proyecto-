# Generated by Django 4.2.1 on 2023-05-19 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seccion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seccion',
            name='descripcion',
            field=models.TextField(max_length=1200),
        ),
        migrations.AlterField(
            model_name='seccion',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='static/resources/img'),
        ),
    ]
