# Generated by Django 2.2.1 on 2019-05-10 13:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Browse', '0002_imagelist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estate',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]