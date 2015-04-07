from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from blogengine import views

sitemaps = {
    'posts': views.PostSitemap,
}

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'personal.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^travel/$', views.home, name='blog-travel'),
    url(r'^posts/(?P<post_slug>[-a-zA-Z0-9]+)/$', views.view_post,
        name='view_post'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': sitemaps}),
)
