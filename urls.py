from django.conf.urls.defaults import patterns, include, url
from portfolio.api import ProjectResource
from portfolio.views import ProjectView

project_resource = ProjectResource();

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^projects/$', ProjectView.as_view()),
    url(r'^api/', include(project_resource.urls)),
    # Examples:
    # url(r'^$', 'portfolio2012.views.home', name='home'),
    # url(r'^portfolio2012/', include('portfolio2012.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
