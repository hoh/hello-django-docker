"""hellodjango URL Configuration
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^hello-world/', include('helloworld.urls')),
    url(r'^admin/', admin.site.urls),
]
