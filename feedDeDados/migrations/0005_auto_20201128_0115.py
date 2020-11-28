# Generated by Django 3.1.3 on 2020-11-28 04:15

import django.core.validators
from django.db import migrations, models
import feedDeDados.validators


class Migration(migrations.Migration):

    dependencies = [
        ('feedDeDados', '0004_auto_20201127_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feeddedados',
            name='nomeArquivo',
            field=models.CharField(db_index=True, max_length=100, unique=True, validators=[django.core.validators.RegexValidator(message='Nome do arquivo de dados precisa ser do formato CSV.', regex='^[a-z]+\\.(csv)$'), feedDeDados.validators.validaArquivo]),
        ),
    ]