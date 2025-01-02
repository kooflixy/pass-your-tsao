# Generated by Django 5.1.4 on 2025-01-02 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('username', models.CharField(max_length=255, verbose_name='Имя')),
                ('email', models.CharField(blank=True, max_length=255, null=True, verbose_name='Почта')),
                ('password', models.CharField(blank=True, max_length=500, null=True, verbose_name='Пароль')),
                ('description', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Описание')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
            ],
        ),
    ]
