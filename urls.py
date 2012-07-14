from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.static import static
from django.http import HttpResponse
from django.conf import settings
from portfolio.api import ProjectResource
from portfolio.views import PortfolioView, FeaturedPortfolioView

project_resource = ProjectResource();

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', FeaturedPortfolioView.as_view()), 
    url(r'^accounts/login/$',  'django.contrib.auth.views.login' ),
    url(r'^accounts/logout/$',  'django.contrib.auth.views.logout', {'next_page':'/'} ),
    url(r'^api/', include(project_resource.urls)),
    url(r'^admin/', include(admin.site.urls)), 
    url(r'^(?P<slug>[\w-]+)/$', PortfolioView.as_view()),
    url(r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /static/", mimetype="text/plain")),
)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
