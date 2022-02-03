from re import template
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render
from django.views import generic

class HomePageView(generic.TemplateView):
    template_name = 'portfolio/homepage.html'

class MediaPageView(generic.ListView):
    template_name = 'portfolio/media.html'

class BandPageView(generic.TemplateView):
    template_name = 'bands.html'

class ContactPageView(generic.TemplateView):
    template_name = 'contact.html'