# Generated by Django 5.0.6 on 2024-06-26 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barRestaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='price_E',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='price_L',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
