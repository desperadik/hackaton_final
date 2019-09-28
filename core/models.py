from django.db import models

from django.contrib.auth.models import User
from django_extensions.db.models import TimeStampedModel

class Employee(TimeStampedModel):
    """
    Модель данных работника
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    university = models.ForeignKey(verbose_name=u'')


class University(TimeStampedModel):
    """
    Справочник ВУЗов
    """


