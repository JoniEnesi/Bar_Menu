# Generated by Django 5.0.6 on 2024-06-26 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barRestaurant', '0005_menu_price_f_e_alter_menu_price_e'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='price_F_E',
        ),
    ]
