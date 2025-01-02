from django import forms

from accounts.models import Account


class AddAccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['name', 'username', 'email', 'password', 'description']

        widgets = {
            'password': forms.PasswordInput(),
        }