from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from users.forms import LoginUserForm, RegisterUserForm

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация'}
    success_url = reverse_lazy('accounts:accounts')

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    extra_content = {'title': 'Регистрация'}
    success_url = reverse_lazy('users:login')
