# Generated by Django 2.0.3 on 2018-03-29 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0003_auto_20180329_1717'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='angry_count',
        ),
        migrations.RemoveField(
            model_name='post',
            name='funny_count',
        ),
        migrations.RemoveField(
            model_name='post',
            name='hashtags',
        ),
        migrations.RemoveField(
            model_name='post',
            name='post_date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='reaction',
        ),
        migrations.RemoveField(
            model_name='post',
            name='reaction_counts',
        ),
        migrations.RemoveField(
            model_name='post',
            name='sad_count',
        ),
        migrations.RemoveField(
            model_name='post',
            name='wow_count',
        ),
    ]
