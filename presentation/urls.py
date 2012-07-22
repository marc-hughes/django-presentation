from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^slide/(?P<slide>[0-9]+)$', 'presentation.views.direct_to_template', {}, "slide"),
)
