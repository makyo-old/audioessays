from django.db import models
from django.contrib.auth.models import User

class Series(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length = 100)
    description = models.TextField()
    owner = models.ForeignKey(User)
    contributors = models.ManyToManyField(User)
    transcriptions_are_free = models.BooleanField(default = "True")

class Episode(models.Model):
    series = models.ForeignKey(Series)
    authors = models.ManyToManyField(User)
    title = models.CharField(max_length = 100)
    description = models.TextField()
    keywords = models.CharField(max_length = 100)
    transcription = models.TextField()
    published = models.BooleanField()
    pub_date = models.DateTimeField(auto_now = True)
    audio_file = models.FileField(upload_to = episode_path)

    def episode_path(instance, filename):
        from time import time
        return "%s/%d.mp3" % (instance.series.slug, int(time()))
