from django.db import models
#from Profile.models import User
from django.contrib.auth.models import User

# Create your models here.
class Estate(models.Model):
    address = models.CharField(max_length=255)
    lotSize = models.IntegerField()
    houseSize = models.IntegerField()
    bedNum = models.IntegerField()
    bathNum = models.IntegerField()
    price = models.IntegerField()
    desc = models.CharField(max_length=999)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField()
    #bæta við, "if no pictures still post"
    #bæta við Estate type

class ImageList(models.Model):
    #should contain a list of image jpg links
    estateId = models.ForeignKey(Estate, on_delete=models.CASCADE)
    imageList = models.CharField(max_length=999, blank=True)
