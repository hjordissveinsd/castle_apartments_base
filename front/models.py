from django.db import models

#Raggi, Andri first attempt
#færa mögulega
class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phoneNumber = models.IntegerField()
    #buy
    #sell

class Estate(models.Model):
    address = models.CharField(max_length=255)
    lotSize = models.IntegerField()
    houseSize = models.IntegerField()
    bedNum = models.IntegerField()
    bathNum = models.IntegerField()
    price = models.IntegerField()
    desc = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField()

class Message (models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE)
    #writer = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=999)

class VisitMessage (models.Model):
    message = models.CharField(max_length=999)
    date = models.DateTimeField()
    estate = models.ForeignKey(Estate, on_delete=models.CASCADE)
    #buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
