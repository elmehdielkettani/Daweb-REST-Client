from django.conf.urls.defaults import *

urlpatterns = patterns('restclient.apps.root.views',
    (r'^$', 'view_default'),
)
