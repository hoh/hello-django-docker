"""hellodjango URL Configuration
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView


urlpatterns = [
    url(r'^$', RedirectView.as_view(pattern_name='list_db_objects')),
    url(r'^hello-world/', include('helloworld.urls')),
    url(r'^admin/', admin.site.urls),
]
