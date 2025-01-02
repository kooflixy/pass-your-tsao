from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

class BelongingManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(owner=get_user_model())

class Account(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    username = models.CharField(max_length=255, verbose_name='Имя')
    email = models.CharField(max_length=255, blank=True, null=True, verbose_name='Почта')
    password = models.CharField(max_length=500, blank=True, null=True, verbose_name='Пароль')
    description = models.TextField(max_length=1000, blank=True, null=True, verbose_name='Описание')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Обновлен')
    # owner = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='accounts', null=True, default=None)

    objects = models.Manager()
    # belonging = BelongingManager()


    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("accounts:account", kwargs={"account_id": self.pk})