# Generated by Django 3.2.8 on 2021-11-26 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('M2A_app', '0020_auto_20211126_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='pergunta',
            name='questionario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='M2A_app.questionario'),
            preserve_default=False,
        ),
    ]