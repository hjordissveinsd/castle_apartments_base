from django.db import models
from Profile.models import User
#from django.contrib.auth.models import User

# Create your models here.
class Estate(models.Model):
    address = models.CharField(max_length=255)
    lotSize = models.IntegerField()
    houseSize = models.IntegerField()
    bedNum = models.IntegerField()
    bathNum = models.IntegerField()
    price = models.IntegerField()
    desc = models.CharField(max_length=999)
    city = models.CharField(max_length=100)
    zip = models.IntegerField(max_length=4)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, initial={{User.pk}})
    status = models.BooleanField(default=True)
    image = models.ImageField(upload_to='es_image/')
    #bæta við, "if no pictures still post"
    #bæta við Estate type
