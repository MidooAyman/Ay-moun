# Generated by Django 4.2 on 2023-04-23 03:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cartapp', '0014_destination_payability'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destination',
            name='payability',
        ),
    ]
