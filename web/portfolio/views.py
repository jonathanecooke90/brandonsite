from re import template
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render
from django.views import generic

from .models import BrandonMedia
from .forms import ContactForm

class HomePageView(generic.TemplateView):
    template_name = 'portfolio/homepage.html'

class MediaPageView(generic.ListView):
    model = BrandonMedia
    template_name = 'portfolio/media.html'
    context_object_name = 'media_list'

class BandPageView(generic.TemplateView):
    template_name = 'bands.html'

class ContactPageView(generic.TemplateView):
    template_name = 'contact.html'