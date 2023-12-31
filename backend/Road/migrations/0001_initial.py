# Generated by Django 4.1 on 2023-12-10 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Road',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=-1)),
                ('num_of_points', models.IntegerField()),
                ('base_color', models.IntegerField()),
                ('hover_color', models.IntegerField()),
                ('crowd', models.IntegerField()),
                ('feedback', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.DecimalField(decimal_places=10, max_digits=15)),
                ('y', models.DecimalField(decimal_places=10, max_digits=15)),
                ('road', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Road.road')),
            ],
        ),
    ]
