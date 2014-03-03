from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()
     
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'blogapp.views.index'),
    url(r'^(?P<year>\d+)/(?P<month>\d+)/(?P<slug>[\w\-]+)/$', 'blogapp.views.post'),
    url(r'^(?P<year>\d+)/(?P<month>\d+)/$', 'blogapp.views.date_index'),
    url(r'^category/(?P<category>\w+)/$', 'blogapp.views.category_index'),
)
