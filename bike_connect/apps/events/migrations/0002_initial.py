# Generated by Django 5.1.3 on 2024-12-07 13:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='organizer',
            field=models.ForeignKey(blank=True, help_text='The user organizing the event. The event will be deleted if the organizer is removed.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='organized_events', to=settings.AUTH_USER_MODEL, verbose_name='Event Organizer'),
        ),
        migrations.AddField(
            model_name='participation',
            name='event',
            field=models.ForeignKey(help_text='The event the user is participating in.', on_delete=django.db.models.deletion.CASCADE, related_name='participants', to='events.event', verbose_name='Event'),
        ),
        migrations.AddField(
            model_name='participation',
            name='user',
            field=models.ForeignKey(help_text='The user participating in the event.', on_delete=django.db.models.deletion.CASCADE, related_name='participations', to=settings.AUTH_USER_MODEL, verbose_name='Participant'),
        ),
        migrations.AlterUniqueTogether(
            name='participation',
            unique_together={('user', 'event')},
        ),
    ]
