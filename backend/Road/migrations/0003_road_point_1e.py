# Generated by Django 4.1 on 2023-11-20 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Road', '0002_road_point_1s_road_point_2e_road_point_2s_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='road',
            name='point_1e',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=10),
        ),
    ]
