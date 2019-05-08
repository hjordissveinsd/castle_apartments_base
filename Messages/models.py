from django.db import models
from Profile.models import User
from Browse.models import Estate


# Create your models here.
class Message (models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE)
    #writer = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=999)

class VisitMessage (models.Model):
    message = models.CharField(max_length=999)
    date = models.DateTimeField()
    property = models.ForeignKey(Estate, on_delete=models.CASCADE)
    #buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)