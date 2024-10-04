# Generated by Django 5.1.1 on 2024-10-03 16:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cronograma', '0002_cronograma_valor'),
        ('pago', '0003_pago_recibo'),
        ('usuarioPadreFamilia', '0002_rename_user_name_usuariopadrefamilia_username_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pago',
            name='cronograma',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cronograma.cronograma'),
        ),
        migrations.AddField(
            model_name='pago',
            name='nombre_pago',
            field=models.CharField(default='Pago genérico', max_length=100),
        ),
        migrations.AddField(
            model_name='pago',
            name='tipo_pago',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='pago',
            name='usuario_padre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarioPadreFamilia.usuariopadrefamilia'),
        ),
        migrations.AlterField(
            model_name='pago',
            name='estado_pago',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='pago',
            name='valor_pago',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]