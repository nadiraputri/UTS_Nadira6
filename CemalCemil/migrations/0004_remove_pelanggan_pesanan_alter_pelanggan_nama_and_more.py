# Generated by Django 5.0.5 on 2024-05-10 05:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CemalCemil', '0003_rename_pembelian_pesanan_meja'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pelanggan',
            name='pesanan',
        ),
        migrations.AlterField(
            model_name='pelanggan',
            name='nama',
            field=models.IntegerField(),
        ),
        migrations.AddField(
            model_name='pelanggan',
            name='Pesanan',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='pelanggan', to='CemalCemil.pesanan'),
            preserve_default=False,
        ),
    ]
