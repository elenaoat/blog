from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models
import datetime
from django.contrib.sitemaps import Sitemap


def home(request):
    # import pdb; pdb.set_trace()
    if 'travel' in request.META['PATH_INFO']:
        last_5 = models.Post.objects.filter(tag='travel').order_by('-pub_date')[:5]
    elif 'tech' in request.META['PATH_INFO']:
        last_5 = models.Post.objects.filter(tag='coding').order_by('-pub_date')[:5]
    else:
        last_5 = models.Post.objects.filter(tag='personal-development').order_by('-pub_date')[:5]

    ctx = {'posts': last_5}

    return render(request, 'home.html', ctx)


def about(request):

    return render(request, 'about.html')


def view_post(request, post_slug):
    post = get_object_or_404(models.Post, slug=post_slug)
    ctx = {'post': post}
    return render(request, 'post.html', ctx)


class PostSitemap(Sitemap):
    changefreq = "daily"
    priority = 1.0
    lastmod = datetime.datetime.now()

    def items(self):
        return models.Post.objects.all()