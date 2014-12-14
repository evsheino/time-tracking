from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout_then_login

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'timetracking.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^timetrack/', include('timetrack.urls', namespace='timetrack')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', login, {'template_name': 'login.html'}),
    url(r'^accounts/logout/$', logout_then_login, name='logout'),
)
