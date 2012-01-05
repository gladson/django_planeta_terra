from django.conf.urls.defaults import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#Projeto Meu Blog
from meu_blog.blog.models import *
from meu_blog.blog.feeds import UltimosArtigos

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'meu_blog.views.home', name='home'),
    # url(r'^meu_blog/', include('meu_blog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    #Blog
    url(r'^$', 'django.views.generic.date_based.archive_index', 
    {'queryset': Artigo.objects.all(),
    'date_field': 'publicacao'}),
    url(r'^rss/(?P<url>.*)/$', 'django.contrib.syndication.views.feed',
    {'feed_dict': {'ultimos': UltimosArtigos}}),
    url(r'^artigo/(?P<artigo_id>\d+)/$', 'meu_blog.blog.views.artigo'),
)
