from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^entry/', ''), # read
    (r'^user/', ''), # list by user
    (r'^series/', ''), # list by series
    (r'^episode/', ''), # list by episode
    (r'^post/', ''), # create entry
    (r'^edit/', ''), # update entry
    (r'^delete/', '') # delete entry
)
