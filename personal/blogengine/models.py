from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now())
    teaser = models.TextField()
    text = models.TextField()
    slug = models.SlugField()

    def __unicode__(self):
        return self.title
