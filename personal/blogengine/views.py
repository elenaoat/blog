from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models


def home(request):
    last_5 = models.Post.objects.order_by('-pub_date')[:5]
    ctx = {'posts': last_5}

    return render(request, 'home.html', ctx)


def about(request):

    return render(request, 'about.html')


def view_post(request, post_slug):
    post = get_object_or_404(models.Post, slug=post_slug)
    ctx = {'post': post}
    return render(request, 'post.html', ctx)
