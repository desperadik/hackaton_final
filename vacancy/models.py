from django.db import models

#
#
# class Candidat(models):

from django.db import models
from django.db.models import Count
from django_extensions.db.models import TimeStampedModel
# from .utils import get_top10, get_vacancy_period

FROM_PARSER = [
    (1, 'Trudvsem'),
    (2, 'hh.ru')
]

class Employer(models.Model):
    """
    Работадатель
    """
    name = models.CharField('Название работадателя', max_length=255 )
    ogrn = models.CharField("ОГРН", max_length=56, blank=True, null=True)
    companycode = models.CharField('ID service', max_length=56, blank=True, null=True)
    inn = models.CharField("ИНН", max_length=56, null=True, blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    """
    Категории
    """
    name = models.CharField("Категория", max_length=255)
    code = models.CharField("Code", max_length=255, null=True, blank=True)
    is_from = models.SmallIntegerField('Откуда получены данные', choices=FROM_PARSER,
                                       blank=True, null=True)

    def cnt_vacancy(self):
        return self.vacancy_set.count()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = "Категории"


class Profession(TimeStampedModel):
    ident = models.CharField(max_length=25)
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name

    @classmethod
    def top(cls):
        return cls.objects.annotate(cnt_vacancy=Count('vacancy', distinct=True))[:10]

    def cnt_vacancy(self):
        return self.vacancy_set.count()

    # def top(self, many_days=180):
    #     """Топ 10 проффесий за последние полгода"""
    #     return get_top10(many_days)


class Vacancy(TimeStampedModel):

    """
    Вакансии
    """
    # Fields to trudvsem
    is_from = models.SmallIntegerField('Откуда получины данные', choices=FROM_PARSER,
                                       blank=True, null=True)
    id_service = models.CharField('id', max_length=55, blank=True, null=True)
    company = models.ForeignKey('Employer', verbose_name="Работадатель", on_delete=models.CASCADE,
                                blank=True, null=True)
    created_dt = models.DateField("Дата создания на сервисе", blank=True, null=True)
    salary = models.CharField("Зарплата", max_length=50, blank=True, null=True)
    salary_min = models.IntegerField("Минимальная ЗП", blank=True, null=True)
    salary_max = models.IntegerField("Максимальная зарплата", blank=True, null=True)
    employment = models.CharField("Трудоустройство", max_length=55, blank=True, null=True)
    schedule = models.CharField("График работы", max_length=55, blank=True, null=True)
    duty = models.TextField(verbose_name="Обязанности", blank=True, null=True)
    category = models.ForeignKey(Category, verbose_name="Категория",
                                 blank=True, null=True, on_delete=models.CASCADE)
    profession = models.ForeignKey(Profession, verbose_name="Профессия",
                                 blank=True, null=True, on_delete=models.CASCADE)
    education = models.CharField("Образование", max_length=150, blank=True)
    qualification = models.TextField("Квалификация", blank=True, null=True)
    experience = models.CharField("Опыт работы", max_length=55, blank=True, null=True)
    address = models.CharField("Адрес", max_length=255, blank=True, null=True)

    title = models.CharField('Название вакансии', max_length=255)
    description = models.TextField('Описание вакансии', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'


class Rating(models.Model):
    """
    Модель рейтингов
    """
    period_start = models.DateField("Начало периода")
    period_end = models.DateField("Конец периода")
    professions = models.ManyToManyField(Profession)


