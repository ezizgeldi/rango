from typing import ClassVar
from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class HomePageView(TemplateView):
    template_name = 'pages/index.html' 

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'



def index(request):
    return render(request, 'pages/index.html')

