# Generated by Django 4.1.5 on 2023-02-13 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formation', '0021_remove_contenir_id_mot_motfr_id_contenir'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='motfr',
            name='id_Contenir',
        ),
        migrations.AddField(
            model_name='contenir',
            name='id_Mot',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='mots', to='formation.motfr'),
            preserve_default=False,
        ),
    ]
