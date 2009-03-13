from django.conf.urls.defaults import *

urlpatterns = patterns('dgci.views',
    url(r'^start/$', 'start'),
    url(r'^return/$', 'return_'),
)

