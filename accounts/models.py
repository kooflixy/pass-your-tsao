from django.contrib.auth import get_user_model
from django.db import models

# class OwnerManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(owner=get_user_model().pk)

class Account(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    username = models.CharField(max_length=255, verbose_name='Имя')
    email = models.CharField(max_length=255, blank=True, null=True, verbose_name='Почта')
    password = models.CharField(max_length=500, blank=True, null=True, verbose_name='Пароль')
    description = models.TextField(max_length=1000, blank=True, null=True, verbose_name='Описание')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Обновлен')