# Generated by Django 4.2.1 on 2023-06-15 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0017_aluno_numero_matricula_turma_matricula_aluno_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turma',
            name='matricula_aluno',
        ),
        migrations.AddField(
            model_name='aluno',
            name='turma',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cadastro.turma'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='turma',
            name='codigo_turma',
            field=models.IntegerField(default=1, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='turma',
            name='numero_matricula',
            field=models.IntegerField(default=43434, unique=True),
            preserve_default=False,
        ),
    ]
