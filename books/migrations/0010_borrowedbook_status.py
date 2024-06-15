# Generated by Django 5.0.6 on 2024-06-15 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_alter_borrowedbook_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrowedbook',
            name='status',
            field=models.CharField(choices=[('borrowed', 'borrowed'), ('returned', 'returned')], default='borrowed', max_length=100),
        ),
    ]
