# Generated by Django 4.2.1 on 2023-06-21 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seccion', '0006_remove_servicios_items_servicios_nombre_delete_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicios',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]
