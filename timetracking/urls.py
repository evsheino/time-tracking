from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'timetracking.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^timetrack/', include('timetrack.urls', namespace='timetrack')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^foundation/', include('foundation.urls')),
)
