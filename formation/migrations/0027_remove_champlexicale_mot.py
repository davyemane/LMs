# Generated by Django 4.1.5 on 2023-02-16 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formation', '0026_champlexicale_mot'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='champlexicale',
            name='mot',
        ),
    ]
