# Generated by Django 5.1.1 on 2024-09-23 11:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
                ('art_url', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform_name', models.CharField(max_length=50, unique=True)),
                ('platform_abbreviation', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publisher_name', models.CharField(max_length=50, unique=True)),
                ('publisher_domain_name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlatformGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='robocritic.game')),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='robocritic.platform')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_url', models.CharField(max_length=200)),
                ('robo_score', models.DecimalField(decimal_places=1, max_digits=3)),
                ('critic_score', models.DecimalField(decimal_places=1, max_digits=3)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='robocritic.game')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='robocritic.publisher')),
            ],
        ),
        migrations.CreateModel(
            name='ReviewCon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cons', models.TextField()),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='robocritic.review')),
            ],
        ),
        migrations.CreateModel(
            name='Reviewer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewer_full_name', models.CharField(max_length=100)),
                ('reviewer_bio_url', models.CharField(blank=True, max_length=100, null=True)),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='robocritic.publisher')),
            ],
        ),
        migrations.AddField(
            model_name='review',
            name='reviewer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='robocritic.reviewer'),
        ),
        migrations.CreateModel(
            name='ReviewPro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pros', models.TextField()),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='robocritic.review')),
            ],
        ),
    ]
