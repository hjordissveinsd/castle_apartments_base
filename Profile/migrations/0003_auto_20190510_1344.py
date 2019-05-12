# Generated by Django 2.2.1 on 2019-05-10 13:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('Browse', '0003_auto_20190510_1344'),
        ('Profile', '0002_profileimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('ssn', models.CharField(blank=True, max_length=30)),
                ('phone', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='ProfileImage',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]