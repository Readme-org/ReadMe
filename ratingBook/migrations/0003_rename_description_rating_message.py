# Generated by Django 4.2.6 on 2023-10-29 02:21

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("ratingBook", "0002_alter_rating_rating"),
    ]

    operations = [
        migrations.RenameField(
            model_name="rating",
            old_name="description",
            new_name="message",
        ),
    ]
