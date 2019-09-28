from django.db import models

from django.contrib.auth.models import User
from django_extensions.db.models import TimeStampedModel


class AbstractOrg(models.Model):
    """
    Абстрактная модель для организаций
    """
    name = models.CharField("Название", max_length=255)
    inn = models.CharField("ИНН", max_length=16)
    desc = models.TextField("Описание")

    class Meta:
        abstract = True
