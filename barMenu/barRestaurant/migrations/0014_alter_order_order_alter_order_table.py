# Generated by Django 5.0.6 on 2024-07-07 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barRestaurant', '0013_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order',
            field=models.TextField(blank=True, max_length=999999999, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='table',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]