from django.conf.urls import patterns, include, url
from LOLHub.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'LOUHub.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    (r'^$', SocialHub),
    (r'^Card/$', StatsCard),
    (r'^Card/(?P<sname>\w{0,50})/$', StatsCard),
    (r'^AddToHub/$', AddToHub),
    (r'^AddToHubP/$', AddToHubP),
    (r'^SocialHub/$', SocialHub),
    (r'^AddToStreamersP/$', AddToStreamersP),
    (r'^AddToStreamers/$', AddToStreamers),
    (r'^matchActual/$', matchActual),
    (r'^GetChamps/$', GetChamps),
    (r'^GetSpells/$', GetSpells),
    (r'^UpdateSummoners/$', UpdateSummoners),
)
