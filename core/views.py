from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class LoginPage(TemplateView):
    template_name = 'auth_login.html'