# Generated by Django 3.2.8 on 2021-10-20 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('M2A_app', '0008_remove_empresa_endereco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='inscricao_estadual',
            field=models.CharField(max_length=500),
        ),
    ]