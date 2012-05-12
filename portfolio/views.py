from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.generic import TemplateView

class ProjectView(TemplateView):
    template_name = 'base.html'

