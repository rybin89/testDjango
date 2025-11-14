from django.db import models
# Модель User из Django
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    '''Добавим поля для нашего пользователя'''
    patronymic = models.CharField(max_length=100, null=True, blank=True, verbose_name='Отчество')
    phone = models.CharField(max_length=20,null=True,blank=True)
    birthday = models.DateField(null=True)
    class Meta:
        verbose_name = "Пользователь" # Для одмин панели указывать название сущности в единственном числе
        verbose_name_plural = "Пользователи" # Для одмин панели указывать название сущности во множественном числе


