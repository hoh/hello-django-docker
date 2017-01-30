from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^(?P<id_>\d+)$', views.say_hello, name='say_hello'),
]
