from django.contrib import admin
from dev.models import Message, UserProfile, Discussion
# Register your models here.

admin.site.register(Message)
admin.site.register(UserProfile)
admin.site.register(Discussion)