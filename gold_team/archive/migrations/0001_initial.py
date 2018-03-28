# Generated by Django 2.0.3 on 2018-03-28 22:02

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('daily_topic', models.CharField(max_length=200)),
                ('next_topic', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['daily_topic'],
            },
        ),
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a hashtag (e.g. #YOLO #Covfefe etc.)', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular post across entire history', primary_key=True, serialize=False)),
                ('is_parent', models.BooleanField()),
                ('text', models.TextField(max_length=256)),
                ('post_date', models.DateTimeField(blank=True, null=True)),
                ('post_time', models.TimeField()),
                ('upvote_count', models.PositiveIntegerField()),
                ('reaction', models.CharField(blank=True, choices=[('a', 'Angry'), ('f', 'Funny'), ('s', 'Sad'), ('w', 'Wow')], help_text='Why did you upvote this post?', max_length=1)),
                ('reaction_counts', models.PositiveIntegerField()),
                ('angry_count', models.PositiveIntegerField()),
                ('funny_count', models.PositiveIntegerField()),
                ('sad_count', models.PositiveIntegerField()),
                ('wow_count', models.PositiveIntegerField()),
                ('feed', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='archive.Feed')),
                ('hashtags', models.ManyToManyField(help_text='give us a #hashtag', to='archive.Hashtag')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('active_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
                ('email', models.CharField(max_length=64)),
            ],
            options={
                'ordering': ['username'],
            },
        ),
        migrations.AddField(
            model_name='topic',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='archive.User'),
        ),
        migrations.AddField(
            model_name='post',
            name='topic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='archive.Topic'),
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='archive.User'),
        ),
    ]
