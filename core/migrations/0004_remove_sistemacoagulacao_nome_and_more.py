# Generated by Django 4.2.4 on 2023-09-11 01:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_sistemacoagulacao_tanqueajusteph_unidadefloculacao_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sistemacoagulacao',
            name='nome',
        ),
        migrations.RemoveField(
            model_name='tanqueajusteph',
            name='nome',
        ),
        migrations.RemoveField(
            model_name='unidadefloculacao',
            name='nome',
        ),
        migrations.RemoveField(
            model_name='unidadeprecipitacao',
            name='nome',
        ),
    ]
