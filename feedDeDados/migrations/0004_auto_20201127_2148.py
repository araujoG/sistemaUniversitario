# Generated by Django 3.1.3 on 2020-11-28 00:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedDeDados', '0003_auto_20201127_2046'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feeddedados',
            options={'get_latest_by': 'dataCarregamento'},
        ),
    ]
