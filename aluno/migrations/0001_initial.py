# Generated by Django 3.1.3 on 2020-11-27 04:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('disciplina', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('matricula', models.CharField(db_index=True, max_length=8, primary_key=True, serialize=False, unique=True)),
                ('curso', models.CharField(max_length=5)),
            ],
            options={
                'db_table': 'aluno',
            },
        ),
        migrations.CreateModel(
            name='DisciplinaCursada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.IntegerField(default=0)),
                ('anoSemestre', models.CharField(default='', max_length=5)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='aluno.aluno')),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='disciplina.disciplina')),
            ],
            options={
                'db_table': 'disciplinaCursada',
                'unique_together': {('disciplina', 'aluno', 'anoSemestre')},
            },
        ),
        migrations.AddField(
            model_name='aluno',
            name='disciplinas',
            field=models.ManyToManyField(blank=True, default='', through='aluno.DisciplinaCursada', to='disciplina.Disciplina'),
        ),
    ]
