from portfolio.models import About

def about_me(request):
    about = About.objects.filter(pk=1)
    about_obj = about[0]

    return {
            'About': about_obj,
     }
