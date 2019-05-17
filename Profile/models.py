from django.db import models
from django.contrib.auth.models import User
from Browse.models import Estate


class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    ssn = models.CharField(max_length=15, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)

class Tracker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.URLField()
    estate = models.ForeignKey(Estate, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'url',)
