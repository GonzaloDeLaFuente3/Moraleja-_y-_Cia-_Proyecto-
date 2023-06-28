# Generated by Django 4.2.1 on 2023-05-19 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Configuraciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono1', models.CharField(max_length=250)),
                ('telefono2', models.CharField(blank=True, max_length=250)),
                ('linkwhatsapp', models.URLField()),
                ('linkfacebook', models.URLField()),
                ('linkinstagram', models.URLField()),
                ('correo_electronico', models.EmailField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]