# Generated by Django 4.1.5 on 2023-02-07 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formation', '0014_alter_champlexicale_niveau'),
    ]

    operations = [
        migrations.AlterField(
            model_name='champlexicale',
            name='Niveau',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='formation.niveauformation'),
        ),
        migrations.AlterField(
            model_name='contenir',
            name='NomChamp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formation.champlexicale'),
        ),
    ]