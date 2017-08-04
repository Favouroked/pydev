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
    user = models.OneToOneField(User)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username