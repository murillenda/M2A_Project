# Generated by Django 3.2.8 on 2021-11-27 23:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('M2A_app', '0024_alter_diagnostico_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuarioinfo',
            old_name='formacao_responsavel',
            new_name='formacao',
        ),
        migrations.AlterField(
            model_name='usuarioinfo',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='info', to=settings.AUTH_USER_MODEL),
        ),
    ]