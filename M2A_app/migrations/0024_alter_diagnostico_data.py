# Generated by Django 3.2.8 on 2021-11-27 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('M2A_app', '0023_auto_20211127_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnostico',
            name='data',
            field=models.DateField(auto_now_add=True),
        ),
    ]