from django.conf.urls import patterns, include, url

urlpatterns= patterns('',
    url(r'^all/$', 'wiki.views.wikis'),
    url(r'^get/(?P<wiki_id>\d+)/$','wiki.views.wiki'),
    url(r'^all/$', 'wiki.views.mywikis'),
    url(r'^get/(?P<mywiki_id>\d+)/$','wiki.views.mywiki'),
    url(r'^create/$','wiki.views.create'),
    url(r'^like/(?P<wiki_id>\d+)/$','wiki.views.like_wiki'),
    url(r'^gete/(?P<wiki_id>\d+)/$', 'wiki.views.editwiki'),
)