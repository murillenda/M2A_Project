# Generated by Django 3.2.8 on 2021-11-27 18:46

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('M2A_app', '0022_rename_texto_resposta_texto_resposta'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diagnostico',
            old_name='fk_empresa',
            new_name='empresa',
        ),
        migrations.RemoveField(
            model_name='diagnostico',
            name='dt_ano',
        ),
        migrations.RemoveField(
            model_name='diagnostico',
            name='fk_consultor',
        ),
        migrations.AddField(
            model_name='diagnostico',
            name='data',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='diagnostico',
            name='questionario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='M2A_app.questionario'),
        ),
        migrations.AlterField(
            model_name='diagnostico',
            name='fase',
            field=models.CharField(default='', max_length=3),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pergunta',
            name='questionario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='perguntas', to='M2A_app.questionario'),
        ),
        migrations.AlterField(
            model_name='resposta',
            name='pergunta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='respostas', to='M2A_app.pergunta'),
        ),
        migrations.CreateModel(
            name='RespostaQuestionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnostico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='M2A_app.diagnostico')),
                ('pergunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='M2A_app.pergunta')),
                ('resposta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='M2A_app.resposta')),
            ],
        ),
    ]