# Generated by Django 4.2.6 on 2023-10-28 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listBook', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mybook',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mybook',
            name='isbn',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
