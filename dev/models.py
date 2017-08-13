from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Message(models.Model):
    subject = models.CharField(max_length=128)
    sender = models.CharField(max_length=128, unique=True)
    reciever = models.ForeignKey(User)
    message = models.TextField(default="Hello")

    def __str__(self):
        return self.subject

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
    status = models.TextField()
    stat_pic = models.ImageField(upload_to='status_images', blank=True)

    def __str__(self):
        return self.uploader