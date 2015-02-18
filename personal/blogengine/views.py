from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models


def home(request):
    last_5 = models.Post.objects.order_by('-pub_date')[:5]
    ctx = {'posts': last_5}

    return render(request, 'home.html', ctx)

