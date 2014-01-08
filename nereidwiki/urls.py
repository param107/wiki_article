from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    (r'^/', include('wiki.urls')),
    url(r'^admin/',include(admin.site.urls)),
    # url(r'^$', 'nereidwiki.views.home', name='home'),
    # url(r'^nereidwiki/', include('nereidwiki.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),url(r'^get/(?P<wiki_id>\d+)/$','wiki.views.wiki'),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'wiki.views.login'),
    url(r'^accounts/auth/$','wiki.views.auth_view'),
    url(r'^all/$','wiki.views.logout'),
    url(r'^accounts/loggedin/$', 'wiki.views.loggedin'),
    url(r'^accounts/invalid/$', 'wiki.views.invalid_login'),
    url(r'^accounts/register/$', 'wiki.views.register_user'),
    url(r'^accounts/register_success/$', 'wiki.views.register_success'),
    #url(r'^get/(?P<body>)/$','wiki.views.editwiki'),


)
