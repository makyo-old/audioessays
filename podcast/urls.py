from django.conf.urls.defaults import *

urlpatterns = patterns('audioessays.podcast.views',
    (r'^$', 'list_podcasts'),
    (r'^series/(?P<podcast_slug>.+)/$', 'show_podcast'),
    (r'^feed/(?P<podcast_slug>.+)/$', 'show_feed'),
    (r'^episode/(?P<episode_id>\d+)/$', 'show_episode'),
    (r'^create/series/$', 'create_series'),
    (r'^create/episode/$', 'create_episode'),
    (r'^edit/series/(?P<podcast_slug>.+)/$', 'edit_series'),
    (r'^edit/episode/(?P<episode_id>\d+)/$', 'edit_episode'),
    (r'^delete/series/(?P<podcast_slug>.+)/$', 'delete_series'),
    (r'^delete/episode/(?P<episode_id>\d+)/$', 'delete_episode'),
)
