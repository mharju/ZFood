from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'web.views.index', name='index'),
    url(r'^accounts/login/$', 'web.views.login', name='login'),
    url(r'^accounts/logout/$', 'web.views.logout', name='logout'),
    url(r'^remove/(?P<id>\d+)/$', 'web.views.remove', name='remove'),
    url(r'^store/$', 'web.views.store', name='store'),
    url(r'^csv/$', 'web.views.csv', name='csv'),
    url(r'^csv/(?P<encoding>.+)$', 'web.views.csv', name='csv'),
)
