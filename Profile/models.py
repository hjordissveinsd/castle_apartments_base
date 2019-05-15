from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#class User(models.Model):
#    name = models.CharField(max_length=255)
#    email = models.CharField(max_length=255)
#    password = models.CharField(max_length=255)
#    username = models.CharField(max_length=255)
#    address = models.CharField(max_length=255)
#    phoneNumber = models.IntegerField()


#class ProfileImage(models.Model):
#    the_image = models.CharField(max_length=999)
#    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    ssn = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)

class Tracker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.URLField()

    class Meta:
        unique_together = ('user', 'url',)
