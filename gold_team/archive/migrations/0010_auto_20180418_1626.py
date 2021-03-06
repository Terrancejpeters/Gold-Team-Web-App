# Generated by Django 2.0.4 on 2018-04-18 20:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0009_auto_20180416_1545'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'permissions': (('can_make_post', 'Make a new post'),)},
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular post across entire history', primary_key=True, serialize=False),
        ),
    ]
