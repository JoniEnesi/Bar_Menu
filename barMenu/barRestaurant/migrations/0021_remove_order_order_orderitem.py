# Generated by Django 5.0.6 on 2024-07-08 13:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barRestaurant', '0020_remove_table_order_order_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order',
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name_al', models.CharField(max_length=50)),
                ('product_name_en', models.CharField(max_length=50)),
                ('qty', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='barRestaurant.order')),
            ],
        ),
    ]
