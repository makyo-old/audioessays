from django.conf.urls.defaults import *

urlpatterns = patterns('audioessays.blog.views',
    (r'^entry/(?P<entry_id>\d+)/$', 'show_entry'),
    (r'^user/(?P<username>.+)/$', 'list_by_user'),
    (r'^series/(?P<podcast_slug>.+)/$', 'list_by_series'),
    (r'^episode/(?P<episode_id>\d+)/$', 'list_by_episode'),
    (r'^post/', 'create_entry'),
    (r'^edit/(?P<entry_id>\d+)/$', 'edit_entry'),
    (r'^delete/(?P<entry_id>\d+)/$', 'delete_entry')
)
