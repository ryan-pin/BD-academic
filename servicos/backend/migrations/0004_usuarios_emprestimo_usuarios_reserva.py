# Generated by Django 5.1.4 on 2024-12-04 18:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_remove_reservas_data_reserva_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='emprestimo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.emprestimos'),
        ),
        migrations.AddField(
            model_name='usuarios',
            name='reserva',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.reservas'),
        ),
    ]
