# Generated by Django 2.2.1 on 2019-05-16 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0002_tracker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='profile',
            name='ssn',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
