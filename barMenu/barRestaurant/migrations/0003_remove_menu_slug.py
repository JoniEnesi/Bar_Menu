# Generated by Django 5.0.6 on 2024-06-26 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barRestaurant', '0002_menu_price_e_menu_price_l'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='slug',
        ),
    ]
