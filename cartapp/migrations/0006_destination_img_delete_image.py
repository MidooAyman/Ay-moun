# Generated by Django 4.2 on 2023-04-20 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartapp', '0005_remove_destination_img_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='img',
            field=models.ImageField(default=1, upload_to='pics'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]