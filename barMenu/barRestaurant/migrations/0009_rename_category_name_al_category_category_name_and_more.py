# Generated by Django 5.0.6 on 2024-07-01 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barRestaurant', '0008_rename_category_name_category_category_name_al_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category_name_al',
            new_name='category_name',
        ),
        migrations.RemoveField(
            model_name='category',
            name='category_name_en',
        ),
    ]