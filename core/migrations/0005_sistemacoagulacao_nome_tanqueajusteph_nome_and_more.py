# Generated by Django 4.2.4 on 2023-09-11 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_sistemacoagulacao_nome_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sistemacoagulacao',
            name='nome',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tanqueajusteph',
            name='nome',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='unidadefloculacao',
            name='nome',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='unidadeprecipitacao',
            name='nome',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
