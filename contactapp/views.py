from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class BasicTemplateView(TemplateView):
    template_name = 'contactapp/base.html'