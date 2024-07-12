# Generated by Django 5.0.6 on 2024-07-11 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barRestaurant', '0027_table_order_table_view_order_delete_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Overview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table', models.IntegerField(blank=True, null=True)),
                ('order', models.TextField(blank=True, max_length=999999999, null=True)),
                ('total', models.IntegerField(blank=True, null=True)),
                ('paid_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='table',
            name='order',
            field=models.TextField(blank=True, editable=False, max_length=999999999, null=True),
        ),
        migrations.AlterField(
            model_name='table',
            name='table',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='table',
            name='total',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
    ]