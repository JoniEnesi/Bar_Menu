# Generated by Django 5.0.6 on 2024-07-08 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barRestaurant', '0021_remove_order_order_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order',
            field=models.TextField(blank=True, max_length=999999999, null=True),
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]