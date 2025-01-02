from django.urls import path

from accounts import views


app_name = 'accounts'

urlpatterns = [
    path('', views.ShowAccounts.as_view(), name='accounts')
]
