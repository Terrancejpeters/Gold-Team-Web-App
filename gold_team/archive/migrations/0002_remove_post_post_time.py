# Generated by Django 2.0.3 on 2018-03-29 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_time',
        ),
    ]
