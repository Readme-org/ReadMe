# Generated by Django 4.1.5 on 2023-10-27 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_profile'),
        ('diskusiBook', '0004_remove_comment_replies_remove_post_comment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diskusiBook.post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='Book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.book'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diskusiBook.comment'),
        ),
    ]