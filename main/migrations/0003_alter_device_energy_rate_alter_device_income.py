# Generated by Django 4.0.3 on 2022-03-17 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_device_device_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='energy_rate',
            field=models.FloatField(max_length=300, verbose_name='Расход за час в киловаттах'),
        ),
        migrations.AlterField(
            model_name='device',
            name='income',
            field=models.FloatField(max_length=300, verbose_name='Доход за час в долларах'),
        ),
    ]
