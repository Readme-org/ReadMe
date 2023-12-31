# Generated by Django 4.2.6 on 2023-10-29 02:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_merge_0007_delete_searchhistory_0008_book_genre'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wishlistBook', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlistbook',
            name='authors',
        ),
        migrations.RemoveField(
            model_name='wishlistbook',
            name='display_title',
        ),
        migrations.RemoveField(
            model_name='wishlistbook',
            name='image',
        ),
        migrations.RemoveField(
            model_name='wishlistbook',
            name='title',
        ),
        migrations.AddField(
            model_name='wishlistbook',
            name='book',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.book'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wishlistbook',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
