# Generated by Django 4.1.5 on 2023-02-03 23:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formation', '0005_traduires_mottraduit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contenir',
            old_name='id_ChampLexicale',
            new_name='id_ChampLexicales',
        ),
    ]