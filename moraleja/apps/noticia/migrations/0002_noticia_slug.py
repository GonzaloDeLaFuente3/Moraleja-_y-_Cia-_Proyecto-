# Generated by Django 4.2.1 on 2023-06-25 01:21

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noticia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='titulo', unique=True),
        ),
    ]