from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Estate(models.Model):
    address = models.CharField(max_length=255, name="Address")
    lotSize = models.IntegerField(name="Lot Size")
    houseSize = models.IntegerField(name="House Size")
    bedNum = models.IntegerField(name="Number of bedrooms")
    bathNum = models.IntegerField(name="Number of bathrooms")
    price = models.IntegerField(name="Price of estate")
    desc = models.CharField(max_length=999, name="Description of estate")
    city = models.CharField(max_length=100, name="City")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    zip = models.IntegerField(name="Postal code")
    status = models.BooleanField()
    image = models.ImageField(upload_to='es_images/', name="Image of estate")
    #bæta við, "if no pictures still post"
    #bæta við Estate type
