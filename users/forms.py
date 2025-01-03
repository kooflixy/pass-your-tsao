from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        label = 'Логин',
        widget=forms.TextInput(attrs={'class': 'input100'}),
    )

    password = forms.CharField(
        label = 'Пароль',
        widget=forms.PasswordInput(attrs={'class': 'input100'}),
    )

    class Meta:
        model = get_user_model
        fields = ['username', 'password']


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(
        label = 'Логин',
        widget = forms.TextInput(attrs={'class': 'input100'}),
    )

    password1 = forms.CharField(
        label = 'Пароль',
        widget=forms.PasswordInput(attrs={'class': 'input100'}),
    )


    password2 = forms.CharField(
        label = 'Повтор пароля',
        widget=forms.PasswordInput(attrs={'class': 'input100'}),
    )

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'email': 'E-mail',
        }

        widgets = {
            'email': forms.EmailInput(attrs={'class': 'input100'}),
        }