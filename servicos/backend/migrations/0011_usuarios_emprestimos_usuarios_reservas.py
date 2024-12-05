# Generated by Django 5.1.4 on 2024-12-04 19:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0010_remove_livros_autores_livros_autores'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='emprestimos',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='emprestimos_usuario', to='backend.emprestimos'),
        ),
        migrations.AddField(
            model_name='usuarios',
            name='reservas',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reservas_usuario', to='backend.reservas'),
        ),
    ]
