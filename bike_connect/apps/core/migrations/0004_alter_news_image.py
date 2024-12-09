# Generated by Django 5.1.3 on 2024-12-09 01:51

import bike_connect.storages
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_news_options_news_tags_news_views_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, max_length=255, null=True, storage=bike_connect.storages.MediaStorage(), upload_to='news_images/', verbose_name='Image'),
        ),
    ]