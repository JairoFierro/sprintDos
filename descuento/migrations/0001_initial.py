# Generated by Django 5.1.1 on 2024-10-03 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Descuento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_aplicacion', models.DateField()),
                ('valor_descuento', models.FloatField()),
            ],
        ),
    ]