# Generated by Django 5.0.4 on 2024-06-09 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_remove_news_unique_identifier'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='unique_identifier',
            field=models.CharField(blank=True, max_length=255, unique=True),
        ),
    ]