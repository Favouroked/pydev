from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Message(models.Model):
    sender = models.CharField(max_length=128)
    reciever = models.CharField(max_length=128)
    message = models.CharField(max_length=500)
    datetime = models.DateTimeField(null=True)

    def __str__(self):
        return self.sender

class UserProfile(models.Model):
    user = models.ForeignKey(User)
    gender = models.CharField(max_length=6, null=True)
    email = models.EmailField(null=True)
    location = models.CharField(max_length=200, null=True)
    school = models.CharField(max_length=50, null=True)
    website = models.URLField(blank=True, null=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username
class Status(models.Model):
    uploader = models.CharField(max_length=50)
    status = models.CharField(max_length=200)
    stat_pic = models.ImageField(upload_to='status_images', blank=True)
    stat_id = models.IntegerField(default=0)

    def __str__(self):
        return self.uploader

class Discussion(models.Model):
    sender = models.CharField(max_length=50)
    msg = models.CharField(max_length=200)
    msg_pic = models.ImageField(upload_to='group_pic', blank=True)
    datetime = models.DateTimeField(null=True)

    def __str__(self):
        return self.sender
