# Generated by Django 5.0.6 on 2024-06-26 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barRestaurant', '0004_alter_menu_price_e'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='price_F_E',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='price_E',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True),
        ),
    ]
