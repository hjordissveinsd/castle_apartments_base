# Generated by Django 2.2.1 on 2019-05-13 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Browse', '0004_estate_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estate',
            name='image',
            field=models.ImageField(blank=True, upload_to='avatars/'),
        ),
    ]