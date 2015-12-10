from django.db import models
from django.utils import timezone
from datetime import datetime
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify


class SlugMixin(models.Model):
    """Automagic slugs
    """

    slug = models.CharField(max_length=255, unique=True)

    class Meta:
        abstract = True

    _slug_from = 'title'
    _slug_field = 'slug'

    def slugify(self, name):
        return slugify(name)

    def update_slug(self, commit=True):
        if not getattr(self, self._slug_field) and getattr(self, self._slug_from):
            setattr(self, self._slug_field, self.generate_slug())

            if commit:
                self.save()

    def is_unique_slug(self, slug):
        qs = self.__class__.objects.filter(**{self._slug_field: slug})
        return not qs.exists()

    def generate_slug(self):
        original_slug = self.slugify(getattr(self, self._slug_from))
        slug = original_slug

        iteration = 1
        while not self.is_unique_slug(slug):
            slug = "%s-%d" % (original_slug, iteration)
            iteration += 1

        return slug

    def save(self, *args, **kwargs):
        self.update_slug(commit=False)

        return super(SlugMixin, self).save(*args, **kwargs)


class Post(SlugMixin, models.Model):
    title = models.CharField(max_length=200, default="")
    pub_date = models.DateTimeField(default=datetime.now)
    teaser = models.TextField()
    tag = models.CharField(max_length=200, default=u'personal-development')
    text = models.TextField()
    # slug = models.SlugField()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('view_post', kwargs={'post_slug': self.slug})


