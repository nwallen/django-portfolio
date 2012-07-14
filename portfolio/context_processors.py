from portfolio.models import About

def about_me(request):
    about = About.objects.filter(pk=1)
    desc = about[0].description
    return {
            'about_me': desc,
        }
