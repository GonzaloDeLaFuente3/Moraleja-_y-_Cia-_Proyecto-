# Generated by Django 4.2.1 on 2023-06-24 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receta',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='media/img'),
        ),
    ]
