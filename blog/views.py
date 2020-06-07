from django.shortcuts import render
from django.views import generic


class IndexView(generic.TemplateView):
    template_name = "blog/index.html"


class AboutView(generic.TemplateView):
    template_name = "blog/about.html"
