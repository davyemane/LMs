# Generated by Django 4.1.5 on 2023-02-04 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formation', '0007_rename_id_mot_contenir_id_mots'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contenir',
            old_name='id_ChampLexicales',
            new_name='id_ChampLexicale',
        ),
        migrations.RenameField(
            model_name='contenir',
            old_name='id_Mots',
            new_name='id_Mot',
        ),
    ]
