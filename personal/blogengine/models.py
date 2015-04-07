from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse


class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now())
    teaser = models.TextField()
    tag = models.CharField(max_length=200, default=u'personal-development')
    text = models.TextField()
    slug = models.SlugField()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('view_post', kwargs={'post_slug': self.slug})