from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from . import models
from .forms import PostForm
import datetime
from django.contrib.sitemaps import Sitemap


def home(request):
    # import pdb; pdb.set_trace()
    if 'travel' in request.META['PATH_INFO']:
        last_10 = models.Post.objects.filter(tag='travel').order_by('-pub_date')[:10]
    elif 'tech' in request.META['PATH_INFO']:
        last_10 = models.Post.objects.filter(tag='coding').order_by('-pub_date')[:10]
    elif 'learning-languages' in request.META['PATH_INFO']:
        last_10 = models.Post.objects.filter(tag='learning-languages').order_by('-pub_date')[:10]
    else:
        last_10 = models.Post.objects.filter(tag='personal-development').order_by('-pub_date')[:10]

    ctx = {'posts': last_10}
    # try:
    return render(request, 'home.html', ctx)
    # except Exception as e:
    #     print e
    #     import pdb; pdb.set_trace()


def about(request):

    return render(request, 'about.html')

def add_post(request):
    # import pdb; pdb.set_trace()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
            # ctx = {'post': post}
            # template = 'post.html'
        else:
            # import pdb; pdb.set_trace()
            return HttpResponseRedirect('.')
    else:
        post_form = PostForm()
        ctx = {'post_form': post_form}
        template = 'add.html'
    return render(request, template, ctx)

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
