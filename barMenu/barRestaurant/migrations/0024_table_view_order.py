# Generated by Django 5.0.6 on 2024-07-09 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barRestaurant', '0023_offer'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='view_order',
            field=models.BooleanField(default=False),
        ),
    ]
