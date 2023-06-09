# Generated by Django 4.2.1 on 2023-06-21 15:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatTopic',
            fields=[
                ('topic', models.TextField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='ChatRoom',
            fields=[
                ('chat_name', models.TextField(max_length=100, primary_key=True, serialize=False)),
                ('updated', models.DateField(auto_now_add=True)),
                ('created', models.DateField(auto_now=True)),
                ('chat_participants', models.ManyToManyField(related_name='chat_participants', to=settings.AUTH_USER_MODEL)),
                ('chat_topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chatting.chattopic')),
                ('chat_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
