# Generated by Django 4.1.5 on 2023-02-03 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formation', '0004_alter_dialogue_audio_traduires'),
    ]

    operations = [
        migrations.AddField(
            model_name='traduires',
            name='motTraduit',
            field=models.CharField(default=1, max_length=100),
        ),
    ]