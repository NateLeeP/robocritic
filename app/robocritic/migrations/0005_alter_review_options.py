# Generated by Django 5.1.1 on 2024-11-05 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('robocritic', '0004_alter_game_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'managed': False, 'ordering': ['-created_at']},
        ),
    ]