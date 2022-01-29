from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render
from django.views import generic

class HomePageView(generic.TemplateView):
    template_name= 'portfolio/homepage.html'