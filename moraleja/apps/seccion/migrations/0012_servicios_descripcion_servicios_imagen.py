# Generated by Django 4.2.1 on 2023-07-10 02:39

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seccion', '0011_alter_historia_descripcion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicios',
            name='descripcion',
            field=ckeditor.fields.RichTextField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='servicios',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='servicios'),
        ),
    ]
