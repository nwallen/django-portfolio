from portfolio.models import Project, Portfolio, FeaturedPortfolio
from django.views.generic import ListView, DetailView, View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# debugging code
import sys
from pprint import pprint
# pprint (public , sys.stderr)


class LoginRequiredMixin(object):
    #Ensures that user must be authenticated in order to access view.

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)


class PublicPortfolioView(DetailView):
    context_object_name = 'portfolio'
    template_name = 'portfolio.html'
    model = Portfolio
    

class ProtectedPortfolioView(LoginRequiredMixin, PublicPortfolioView):
    model = Portfolio


class PortfolioView(View):
    # staticmethod to avoid adding 'self' to the arguments
    public_view = staticmethod(PublicPortfolioView.as_view())
    protected_view = staticmethod(ProtectedPortfolioView.as_view())

    def dispatch(self, request, *args, **kwargs):

        public = True
        object = Portfolio.objects.filter(slug=kwargs['slug'])
        if len(object) > 0:
            public = object[0].public

        if public:
            return self.public_view(request, *args, **kwargs)
        else:
            return self.protected_view(request, *args, **kwargs)   
            
            
class FeaturedPortfolioView(View):

    portfolio_view = staticmethod(PortfolioView.as_view())
    
    def dispatch(self, request, *args, **kwargs):
        featured = FeaturedPortfolio.objects.filter(pk=1)
        kwargs['slug'] = featured[0].portfolio.slug

        return self.portfolio_view(request, *args, **kwargs)

        
