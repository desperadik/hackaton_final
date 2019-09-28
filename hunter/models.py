from django.contrib.auth.models import User
from django.db import models
from core.models import AbstractOrg, AbstractTypeDir


class TypeOrg(AbstractTypeDir):
    """
    Справочник типов организаций
    """
    pass

    class Meta:
        verbose_name = 'Тип организации'
        verbose_name_plural = 'Типы организаций'


class Org(AbstractOrg):
    """"
    Организации, работодатели
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.ForeignKey(TypeOrg, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'


class Career(models.Model):
    """
    Карьера пользователя
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    org = models.ForeignKey(Org, on_delete=models.CASCADE)
    period = models.DateField("Дата начала", auto_now_add=True)
    period_end = models.DateField("Дата завершения", blank=True, null=True)
    profession = models.ForeignKey('education.Profession', blank=True, null=True, on_delete=models.CASCADE)
