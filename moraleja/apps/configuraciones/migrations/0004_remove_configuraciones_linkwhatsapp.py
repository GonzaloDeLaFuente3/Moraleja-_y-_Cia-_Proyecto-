# Generated by Django 4.1.7 on 2023-06-30 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("configuraciones", "0003_alter_configuraciones_options"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="configuraciones",
            name="linkwhatsapp",
        ),
    ]