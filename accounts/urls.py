from django.urls import path

from accounts import views


app_name = 'accounts'

urlpatterns = [
    path('', views.ShowAccountsList.as_view(), name='accounts'),
    path('<int:account_id>/', views.ShowAccount.as_view(), name='account'),
]
