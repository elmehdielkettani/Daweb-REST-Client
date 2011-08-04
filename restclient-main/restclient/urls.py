from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^proxy/', include("restclient.apps.proxy.urls")),
    (r'^$', include("restclient.apps.root.urls")),
)

