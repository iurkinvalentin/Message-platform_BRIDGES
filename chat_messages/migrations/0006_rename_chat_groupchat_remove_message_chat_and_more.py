# Generated by Django 5.1.1 on 2024-10-30 11:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_messages', '0005_privatechat'),
        ('groups', '0004_groupinvitation_invited_to'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Chat',
            new_name='GroupChat',
        ),
        migrations.RemoveField(
            model_name='message',
            name='chat',
        ),
        migrations.RemoveField(
            model_name='message',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='message',
            name='group_chat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='chat_messages.groupchat'),
        ),
        migrations.AddField(
            model_name='message',
            name='private_chat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='chat_messages.privatechat'),
        ),
    ]
