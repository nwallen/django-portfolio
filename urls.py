from django.conf.urls.defaults import patterns, include, url
from portfolio.api import ProjectResource
from portfolio.views import PortfolioView, FeaturedPortfolioView

project_resource = ProjectResource();

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', FeaturedPortfolioView.as_view()), 
    url(r'^login/$',  'django.contrib.auth.views.login' ),
    url(r'^logout/$',  'django.contrib.auth.views.logout', {'next_page':'/'} ),
    url(r'^api/', include(project_resource.urls)),
    # Examples:
    # url(r'^$', 'portfolio2012.views.home', name='home'),
    # url(r'^portfolio2012/', include('portfolio2012.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)), 
    url(r'^(?P<slug>[\w-]+)/$', PortfolioView.as_view()),
)
