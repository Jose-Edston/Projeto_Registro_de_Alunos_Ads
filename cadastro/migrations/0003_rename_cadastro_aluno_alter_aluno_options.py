# Generated by Django 4.2.1 on 2023-06-10 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0002_rename_contatos_cadastro'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cadastro',
            new_name='Aluno',
        ),
        migrations.AlterModelOptions(
            name='aluno',
            options={'verbose_name_plural': 'Cadastro'},
        ),
    ]
