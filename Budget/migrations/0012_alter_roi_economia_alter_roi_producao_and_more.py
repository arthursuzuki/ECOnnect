# Generated by Django 4.2 on 2023-11-23 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Budget', '0011_alter_roi_economia_alter_roi_producao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roi',
            name='economia',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='roi',
            name='producao',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='roi',
            name='roiResult',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='roi',
            name='tempoROI',
            field=models.FloatField(null=True),
        ),
    ]