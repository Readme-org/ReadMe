# Generated by Django 4.2.6 on 2023-10-28 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WishlistBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('display_title', models.CharField(max_length=255)),
                ('authors', models.TextField()),
                ('image', models.TextField()),
            ],
        ),
    ]
