from django.conf.urls import url
from dev import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^message/$', views.message, name='message'),
    url(r'^people/$', views.user_list, name='users'),
    url(r'^profilereg/$', views.update_profile, name='profile_reg'),
    url(r'^show_profile/(?P<username>[a-zA-Z0-9]+)$', views.show_profile, name='show_profile'),
]
