# Generated by Django 5.0 on 2023-12-13 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Road', '0002_road_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='road',
            name='base_color',
        ),
        migrations.RemoveField(
            model_name='road',
            name='hover_color',
        ),
    ]