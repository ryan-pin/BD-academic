# Generated by Django 5.1.3 on 2024-12-04 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_autor_usuarios_remove_servico_cliente_editoras_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservas',
            name='data_reserva',
        ),
        migrations.RemoveField(
            model_name='reservas',
            name='data_validade',
        ),
    ]
