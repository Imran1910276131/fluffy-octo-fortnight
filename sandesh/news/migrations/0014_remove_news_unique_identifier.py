# Generated by Django 5.0.4 on 2024-06-09 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0013_news_unique_identifier'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='unique_identifier',
        ),
    ]
