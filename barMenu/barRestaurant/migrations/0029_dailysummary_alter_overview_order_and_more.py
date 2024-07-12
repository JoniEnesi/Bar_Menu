# Generated by Django 5.0.6 on 2024-07-12 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barRestaurant', '0028_overview_alter_table_order_alter_table_table_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailySummary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, unique=True)),
                ('products', models.TextField(blank=True, editable=False, max_length=999999999, null=True)),
                ('total_sales', models.IntegerField(default=0, editable=False)),
            ],
        ),
        migrations.AlterField(
            model_name='overview',
            name='order',
            field=models.TextField(blank=True, editable=False, max_length=999999999, null=True),
        ),
        migrations.AlterField(
            model_name='overview',
            name='table',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='overview',
            name='total',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
    ]