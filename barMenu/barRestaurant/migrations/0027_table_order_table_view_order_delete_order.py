# Generated by Django 5.0.6 on 2024-07-09 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barRestaurant', '0026_table_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='order',
            field=models.TextField(blank=True, max_length=999999999, null=True),
        ),
        migrations.AddField(
            model_name='table',
            name='view_order',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]