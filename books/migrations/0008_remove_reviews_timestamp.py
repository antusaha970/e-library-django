# Generated by Django 5.0.6 on 2024-06-15 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_reviews_rating_reviews_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews',
            name='timestamp',
        ),
    ]
