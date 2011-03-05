from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^zfood/', include('zfood.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),

    (r'^$', 'web.views.index',),
    url(r'^remove/(?P<id>\d+)/', 'web.views.remove', name='remove'),
    url(r'^store/', 'web.views.store', name='store'),
    url(r'^csv/', 'web.views.csv', name='csv'),
)
