# Generated by Django 4.2.16 on 2024-11-25 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("robocritic", "0019_alter_review_options_alter_reviewcon_options_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="platformgame",
            options={"managed": False},
        ),
        migrations.AlterModelOptions(
            name="review",
            options={"managed": False, "ordering": ["-created_at"]},
        ),
        migrations.AlterModelOptions(
            name="reviewcon",
            options={"managed": False},
        ),
        migrations.AlterModelOptions(
            name="reviewpro",
            options={"managed": False},
        ),
    ]
