# Generated by Django 4.0.3 on 2022-03-03 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inicio', '0009_alter_nuestrosservicios_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='nuestrosservicios',
            name='breve_descripcion',
            field=models.CharField(blank=True, help_text='>Texto de no mas de 200 caracteres', max_length=200, null=True),
        ),
    ]