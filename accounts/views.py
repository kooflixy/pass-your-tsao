from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView

from accounts.forms import AddAccountForm
from accounts.models import Account
from accounts.utils import DataMixin

class ShowAccountsList(DataMixin, ListView):
    template_name = 'accounts/accounts_list.html'
    context_object_name = 'accounts'
    title_page = 'Аккаунты'

    def get_queryset(self):
        return Account.objects.get_queryset()

class ShowAccount(DataMixin, DetailView):
    model = Account
    template_name = 'accounts/account.html'
    account_id_kwarg = 'account_id'
    context_object_name = 'account'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title = context['account'].name)

    def get_object(self, queryset=None):
        return get_object_or_404(Account.objects, id=self.kwargs[self.account_id_kwarg])

class AddAccount(DataMixin, CreateView):
    form_class = AddAccountForm
    title_page = 'Добавление аккаунта'
    template_name = 'accounts/add_account.html'

    def form_valid(self, form):
        form.save(commit=False)
        return super().form_valid(form)