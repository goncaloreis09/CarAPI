# Generated by Django 4.1.5 on 2023-01-20 20:06

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('line', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chassi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=15)),
                ('year_created', models.IntegerField()),
                ('year_end_of_production', models.IntegerField()),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2023, 1, 20, 20, 6, 12, 85870))),
                ('line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='line.line')),
            ],
        ),
    ]
