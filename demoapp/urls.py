from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin 
admin.autodiscover() 

urlpatterns = patterns('demoapp.views',
    url(r'^$', 'homepage', name='home'),
    url(r'^people$', 'people', name='people'),
    url(r'^follow/(?P<person_id>[0-9]+)$', 'follow', name='follow'),
)
