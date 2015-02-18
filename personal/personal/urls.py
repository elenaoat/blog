from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from blogengine import views
urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'personal.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
