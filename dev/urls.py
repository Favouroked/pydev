from django.conf.urls import url
from dev import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^message/$', views.message, name='message'),
]
