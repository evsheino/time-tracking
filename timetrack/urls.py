from django.conf.urls import patterns, url
from timetrack import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<work_entry_id>\d+)/$', views.show_entry, name='show_entry'),
    url(r'^new/$', views.new_entry, name='new_entry'),
)
