from django.db import models

from Profile.models import User

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
