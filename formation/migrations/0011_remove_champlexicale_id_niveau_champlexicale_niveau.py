# Generated by Django 4.1.5 on 2023-02-07 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formation', '0010_remove_contenir_id_niveau_champlexicale_id_niveau'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='champlexicale',
            name='id_Niveau',
        ),
        migrations.AddField(
            model_name='champlexicale',
            name='Niveau',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='NiveauFormation', to='formation.niveauformation'),
        ),
    ]