# Generated by Django 4.1.5 on 2023-01-20 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0002_engine_fuel_engine_year_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='engine',
            name='fuel',
            field=models.CharField(choices=[('G', 'Gas'), ('D', 'Diesel'), ('E', 'Eletric'), ('H', 'Hybrid')], max_length=1),
        ),
        migrations.AlterField(
            model_name='engine',
            name='year_created',
            field=models.IntegerField(),
        ),
    ]