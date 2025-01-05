from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseNotFound
from accounts.forms import AddAccountForm
from accounts.models import Account
from accounts.utils import DataMixin

def home(request):
    data = {
        'title': 'Главная',
        'user': request.user,
    }
    return render(request, template_name='accounts/home.html')

class ShowAccountsList(LoginRequiredMixin, DataMixin, ListView):
    template_name = 'accounts/accounts_list.html'
    context_object_name = 'accounts'
    title_page = 'Аккаунты'

    def get_queryset(self):
        return Account.belonging.get_queryset(user=self.request.user)


class ShowAccount(LoginRequiredMixin, DataMixin, DetailView):
    model = Account
    template_name = 'accounts/account.html'
    account_id_kwarg = 'account_id'
    context_object_name = 'account'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title = context['account'].name)

    def get_object(self, queryset=None):
        return get_object_or_404(Account.belonging.get_queryset(user=self.request.user), id=self.kwargs[self.account_id_kwarg])


class AddAccount(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddAccountForm
    title_page = 'Добавление аккаунта'
    template_name = 'accounts/add_account.html'

    def form_valid(self, form):
        account = form.save(commit=False)
        account.owner = self.request.user
        return super().form_valid(form)

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')