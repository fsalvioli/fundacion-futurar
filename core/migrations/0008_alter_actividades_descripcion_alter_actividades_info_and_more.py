# Generated by Django 4.2.4 on 2024-06-21 23:28

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0007_alter_donacionescbu_cbu"),
    ]

    operations = [
        migrations.AlterField(
            model_name="actividades",
            name="descripcion",
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name="actividades",
            name="info",
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name="articulos",
            name="articulos",
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name="donaciones",
            name="historial",
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name="donaciones",
            name="info_impacto",
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name="historias",
            name="testimonios",
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name="nosotros",
            name="contenido",
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name="nosotros",
            name="mision",
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name="programas",
            name="contenido",
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name="programas",
            name="info",
            field=ckeditor.fields.RichTextField(),
        ),
    ]