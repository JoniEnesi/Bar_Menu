# Generated by Django 5.0.6 on 2024-07-09 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barRestaurant', '0024_table_view_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='view_order',
        ),
        migrations.AddField(
            model_name='order',
            name='view_order',
            field=models.BooleanField(default=False),
        ),
    ]
