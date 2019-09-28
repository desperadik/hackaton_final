from django.db import models

from django.contrib.auth.models import User
from django_extensions.db.models import TimeStampedModel

class Employee(TimeStampedModel):
    """
    Модель данных работника
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    university = models.ForeignKey('core.University', verbose_name=u'Университет', on_delete=models.CASCADE)


class University(TimeStampedModel):
    """
    Справочник ВУЗов
    """


