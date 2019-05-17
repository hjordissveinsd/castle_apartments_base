from django.db import models
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
    city = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    #setja default value sem active user
    city = models.CharField(max_length=101)
    zip = models.IntegerField()
    status = models.BooleanField()
    #setja defualt value sem true
    image = models.ImageField(upload_to='es_images/')





class Search(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    search_input = models.CharField(max_length=200)

    class Meta:
        unique_together = ('user', 'search_input',)