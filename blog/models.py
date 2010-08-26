from django.db import models
from django.contrib.auth.models import User

class Entry(models.Model):
    owner = models.ForeignKey(User)
    ctime = models.DateTimeField(auto_now_add = True)
    title = models.CharField(max_length = 250)
    body = models.TextField()
