from django.conf.urls.defaults import *

urlpatterns = patterns('restclient.apps.proxy.views',
    (r'^url/$', 'call_proxy'),
    (r'^acu/$', 'autocomplete_urls'),
)
