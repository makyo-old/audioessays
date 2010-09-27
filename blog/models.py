from django.db import models
from django.contrib.auth.models import User
from audioessays.podcast.models import *

class Entry(models.Model):
    owner = models.ForeignKey(User)
    regarding_series = models.ForeignKey(Series, null = True)
    regarding_episode = models.ForeignKey(Episode, null = True)
    ctime = models.DateTimeField(auto_now_add = True)
    mtime = models.DateTimeField(auto_now = True)
    published = models.BooleanField(default = True)
    title = models.CharField(max_length = 250)
    body = models.TextField()
