from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'JonTomBraam.views.home', name='home'),
    url(r'^aboutme/$', 'JonTomBraam.views.aboutme', name='aboutme'),
    url(r'^blog/$', 'JonTomBraam.views.blog', name='blog'),
    url(r'^projects/$', 'JonTomBraam.views.projects', name='projects'),
    url(r'^resume/$', 'JonTomBraam.views.resume', name='resume'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
