from django.conf.urls import url
from dev import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^message/$', views.message, name='message'),
    url(r'^people/$', views.user_list, name='users'),
    url(r'^profilereg/$', views.update_profile, name='profile_reg'),
    url(r'^show_profile/(?P<username>[a-zA-Z0-9]+)$', views.show_profile, name='show_profile'),
    url(r'^status/$', views.status, name='status'),
    url(r'^upload_status/$', views.upload_status, name='upload_status'),
    url(r'^send_msg/$', views.send_discus, name='send_msg'),
    url(r'^show_msg/$', views.show_discus, name='show_msg'),
]
