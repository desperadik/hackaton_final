from django.db import models

from django.contrib.auth.models import User
from django_extensions.db.models import TimeStampedModel


class TimeStamp(models.Model):
    """
    Абстрактная модель дат сохранен/изменен объект
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AbstractOrg(TimeStamp):
    """
    Абстрактная модель для организаций
    """
    name = models.CharField("Название", max_length=255)
    inn = models.CharField("ИНН", max_length=16)
    description = models.TextField("Описание")

    class Meta:
        abstract = True


class AbstractTypeDir(TimeStamp):
    """
    Абстрактная модель для справочников типов
    """
    name = models.CharField("Название", max_length=255)
    description = models.TextField("Описание")


class Profile(models.Model):
    """
    Профиль пользователя
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField("Имя", max_length=30, blank=True)
    last_name = models.CharField("Фамилия", max_length=30, blank=True)
    patronymic_name = models.CharField(verbose_name=u'Отчество', max_length=30, blank=True, null=True)
    avatar = models.ImageField('Аватар')

    def __str__(self):
        return self.last_name

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'
