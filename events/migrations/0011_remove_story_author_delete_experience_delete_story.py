# Generated by Django 5.0.6 on 2024-11-28 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_alter_event_options_remove_event_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story',
            name='author',
        ),
        migrations.DeleteModel(
            name='Experience',
        ),
        migrations.DeleteModel(
            name='Story',
        ),
    ]
