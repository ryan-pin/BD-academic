# Generated by Django 5.1.3 on 2024-12-04 14:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('social_midia', models.CharField(max_length=100)),
                ('endereço', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='servico',
            name='cliente',
        ),
        migrations.CreateModel(
            name='Editoras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('ano', models.IntegerField(verbose_name='Ano de fundação')),
                ('localização', models.CharField(max_length=200)),
                ('autores', models.ManyToManyField(to='backend.autor')),
            ],
        ),
        migrations.CreateModel(
            name='Livros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('ano', models.IntegerField(verbose_name='Data de Publicação')),
                ('foto_capa', models.ImageField(upload_to='uploads/')),
                ('quantidade', models.IntegerField(verbose_name='Quantidade de exemplares')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.autor')),
            ],
        ),
        migrations.CreateModel(
            name='Reservas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_reserva', models.DateField(auto_now_add=True)),
                ('data_validade', models.DateField(blank=True, null=True)),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.livros')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.usuarios')),
            ],
        ),
        migrations.CreateModel(
            name='Emprestimos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.livros')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.usuarios')),
            ],
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.DeleteModel(
            name='Servico',
        ),
    ]