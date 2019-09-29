from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import TemplateView, FormView

from django.views.generic.edit import ProcessFormView

class IndexPage(TemplateView):
    template_name = 'landing/index.html'

class LoginPage(TemplateView, ProcessFormView):
    template_name = 'landing/auth_login.html'

    def post(self, request, *args, **kwargs):
        """ Имитация авторизации ЕСИА"""

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('dashboard_index'))


class DashBoardIndex(TemplateView):

    template_name = 'dashboard/index.html'


def create_employ(request):
    if request.method.POST:
        print(request.POST)
    pass