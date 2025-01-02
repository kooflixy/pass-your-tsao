from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from accounts.models import Account
from accounts.utils import DataMixin

class ShowAccounts(DataMixin, ListView):
    template_name = 'accounts/accounts_list.html'
    context_object_name = 'accounts'
    title_page = 'Аккаунты'

    def get_queryset(self):
        return Account.objects.get_queryset()