# Generated by Django 4.2 on 2023-04-23 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartapp', '0017_alter_destination_des'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Product Name'),
        ),
    ]
