from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

class HomePageViews(TemplateView):
    template_name = "h_pages/home.html"


class AboutUs(TemplateView):
    template_name = "h_pages/about.html"
