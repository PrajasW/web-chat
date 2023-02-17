from django.db import models

# Create your models here.
class Message(models.Model):
    sender = models.CharField(max_length=100)
    reciver = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)
    date = models.CharField(max_length=20)
    time = models.CharField(max_length=20)