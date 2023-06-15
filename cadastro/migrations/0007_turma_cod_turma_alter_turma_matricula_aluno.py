# Generated by Django 4.2.1 on 2023-06-15 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0006_turma_media_notas_alter_turma_matricula_aluno'),
    ]

    operations = [
        migrations.AddField(
            model_name='turma',
            name='cod_turma',
            field=models.IntegerField(default=1, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='turma',
            name='matricula_aluno',
            field=models.IntegerField(),
        ),
    ]
