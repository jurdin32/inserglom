# Generated by Django 4.0.3 on 2022-03-03 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inicio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sliderprincipal',
            name='texto1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sliderprincipal',
            name='texto2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
