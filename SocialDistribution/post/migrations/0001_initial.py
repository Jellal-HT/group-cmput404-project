# Generated by Django 4.1.2 on 2022-11-24 03:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import post.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, default='No Title', max_length=255, null=True)),
                ('source', models.URLField(blank=True, default='https://team9-socialdistribution.herokuapp.com/', null=True)),
                ('origin', models.URLField(default='https://team9-socialdistribution.herokuapp.com/')),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('contentType', models.CharField(choices=[('text/markdown', 'text/markdown'), ('text/plain', 'text/plain'), ('application/base64', 'application/base64'), ('image/png;base64', 'image/png;base64'), ('image/jpeg;base64', 'image/jpeg;base64')], default='text/plain', max_length=255)),
                ('content', models.TextField(blank=True, null=True)),
                ('categories', models.TextField(default='[]', null=True)),
                ('image_url', models.URLField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=post.models.post_upload_to)),
                ('count', models.IntegerField(default=0)),
                ('published', models.DateTimeField(auto_now=True)),
                ('visibility', models.CharField(choices=[('PUBLIC', 'PUBLIC'), ('FRIENDS', 'FRIENDS')], default='PUBLIC', max_length=15)),
                ('unlisted', models.BooleanField(default=False)),
                ('url', models.URLField(editable=False, max_length=500)),
                ('comments', models.URLField(default='<django.db.models.fields.URLField>/comments', editable=False, max_length=500)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-published'],
            },
        ),
        migrations.CreateModel(
            name='Inbox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_type', models.CharField(choices=[('post', 'post'), ('comment', 'comment'), ('like', 'like'), ('follow', 'follow')], max_length=20, null=True)),
                ('object_id', models.UUIDField(null=True)),
                ('published', models.DateTimeField(auto_now_add=True)),
                ('message', models.CharField(default='No message', max_length=500)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-published'],
            },
        ),
    ]
