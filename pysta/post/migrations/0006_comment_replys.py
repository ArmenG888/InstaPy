# Generated by Django 4.0.4 on 2022-05-08 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='replys',
            field=models.ManyToManyField(default='', related_name='comment_replys', to='post.reply'),
        ),
    ]
