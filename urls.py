from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^blog/', include('audioessays.blog.urls')),
    (r'^podcast/', include('audioessays.podcast.urls')),
    (r'^user/', include('audioessays.usermgmt.urls')),
    (r'^accounts/', include('audioessays.usermgmt.account_urls')),
    (r'^admin/', include(admin.site.urls)),
)
