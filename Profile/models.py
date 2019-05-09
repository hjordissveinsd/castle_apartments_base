from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phoneNumber = models.IntegerField()


class ProfileImage(models.Model):
    the_image = models.CharField(max_length=999)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
