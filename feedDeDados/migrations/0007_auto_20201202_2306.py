# Generated by Django 3.1.3 on 2020-12-03 02:06

import django.core.validators
from django.db import migrations, models
import feedDeDados.validators


class Migration(migrations.Migration):

    dependencies = [
        ('feedDeDados', '0006_auto_20201129_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feeddedados',
            name='nomeArquivo',
            field=models.CharField(db_index=True, max_length=100, unique=True, validators=[django.core.validators.RegexValidator(message='O arquivo de dados precisa ser do formato CSV.', regex='^[a-z0-9A-Z]+\\.csv$'), feedDeDados.validators.validaNomeArquivo]),
        ),
    ]
