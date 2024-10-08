# Generated by Django 5.0.6 on 2024-07-12 13:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0012_alter_inicio_imagen"),
    ]

    operations = [
        migrations.RenameField(
            model_name="inicio",
            old_name="mensaje",
            new_name="bienvenida",
        ),
        migrations.RenameField(
            model_name="inicio",
            old_name="ofertas",
            new_name="que_ofrecemos",
        ),
        migrations.AddField(
            model_name="inicio",
            name="publicado",
            field=models.BooleanField(default=False),
        ),
    ]
