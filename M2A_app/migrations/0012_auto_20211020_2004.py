# Generated by Django 3.2.8 on 2021-10-20 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('M2A_app', '0011_auto_20211020_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='celular',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='telefone',
            field=models.CharField(max_length=500),
        ),
    ]