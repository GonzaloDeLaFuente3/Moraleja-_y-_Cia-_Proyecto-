# Generated by Django 4.2.1 on 2023-06-24 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticia', '0002_alter_noticia_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='media/noticias'),
        ),
    ]
