from django.contrib.auth.models import User, AbstractUser
from django.db import models
from core.models import AbstractOrg
from hunter.models import Career
from region.models import Region


class VisibleManager(models.Manager):
    """
    Менаджер активных объектов
    """
    def get_queryset(self):
        kwargs = {"visible": True}
        return super(VisibleManager, self).get_queryset().filter(**kwargs)


class TypeOrg(models.Model):
    """
    Типы учебных заведений
    """
    name = models.CharField("Тип обрахзовательной организации", help_text="Например:  Технический, Гуманитарный и тп",
                            max_length=100)

    def __str__(self):
        return self.name


class StudyForm(models.Model):
    """
    Форма обучения
    """
    name = models.CharField('Название', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'форма обучения'
        verbose_name_plural = 'формы обучения'


class Qualification(models.Model):
    name = models.CharField('Название', max_length=255, db_index=True)
    image = models.ImageField("Картинка", max_length=255, blank=True, null=True)
    short_preview = models.TextField('Краткое описание', null=True, max_length=355,
                                     blank=True)
    description = models.TextField('Описание', null=True, blank=True)
    order_index = models.DecimalField(default=0, max_digits=2, decimal_places=0, blank=True, verbose_name='Порядок', db_index=True)
    pluse = models.TextField(
        'Плюсы',
        null=True, blank=True,)
    cons = models.TextField(
        'Минусы',
        null=True, blank=True,)
    description_end = models.TextField(
        'Описание2',
        null=True, blank=True,)
    slug = models.SlugField('Slug', null=True, blank=True, db_index=True)
    update_date = models.DateTimeField('Обновлено', auto_now=True)

    class Meta:
        ordering = ['order_index']
        verbose_name = 'квалификация'
        verbose_name_plural = 'квалификации'

    def __str__(self):
        return self.name
        

class EduOrg(AbstractOrg):
    """
    Образовательная организация
    """
    typeorg = models.ForeignKey(TypeOrg, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ProfessionGroup(models.Model):
    """группа профессий"""
    slug = models.SlugField('Slug', null=True, blank=True, db_index=True)
    name = models.CharField('Название', max_length=255, db_index=True)
    image = models.ImageField("Картинка", max_length=255, blank=True, null=True)
    update_date = models.DateTimeField('Обновлено', auto_now=True)
    description = models.TextField('Описание', null=True, blank=True,)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = 'группа профессий'
        verbose_name_plural = 'Группы профессий'


class Profession(models.Model):
    """Профессии"""
    group = models.ForeignKey(
        ProfessionGroup,
        null=True, blank=True,
        verbose_name='группа профессий',
        related_name='professions', on_delete=models.CASCADE)

    image = models.ImageField("Картинка", max_length=255, blank=True, null=True)
    name = models.CharField('Название', max_length=255)
    short_description = models.CharField('Краткое описание', max_length=150, blank=True, null=True)
    description = models.TextField('Описание', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = 'профессия'
        verbose_name_plural = 'профессии'

    
class SpecialtyGroup(models.Model):
    """
    Группа специалностей
    """
    
    slug = models.SlugField('Slug', null=True, blank=True, db_index=True)
    name = models.CharField('Название', max_length=255, db_index=True)
    image = models.ImageField("Картинка", max_length=255, blank=True, null=True)
    update_date = models.DateTimeField('Обновлено', auto_now=True)
    description = models.TextField('Описание', null=True, blank=True,)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = 'группа специальностей'
        verbose_name_plural = 'группы специальностей'

    def get_speciality_count(self):
        count = 0
        for direction in self.specialtydirection_set.all():
            count = count + direction.specialty_set.count()
        return count

    def get_speciality_count_ege(self):
        count = 0
        for direction in self.specialtydirection_set.all():
            count = count + direction.specialty_set.count()
        return count


class SpecialtyDirection(models.Model):
    """направление специальностей"""
    name = models.CharField('Название', max_length=255, db_index=True)
    code = models.CharField(verbose_name='Код направления', max_length=10, db_index=True)
    description = models.TextField('Описание', null=True, blank=True)
    group = models.ForeignKey(
        SpecialtyGroup,
        verbose_name='Группа специальностей',
        null=True, blank=True, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = 'направление специальностей'
        verbose_name_plural = 'направления специальностей'


class Specialty(models.Model):
    """
    Специальности
    """
    cover = models.ImageField("image")
    code = models.CharField(verbose_name='Код специальности', max_length=10, db_index=True)
    name = models.CharField('Название', max_length=255, db_index=True)
    professions = models.ManyToManyField(
        Profession,
        blank=True,
        verbose_name='Профессии')
    update_date = models.DateTimeField('Обновлено', auto_now=True)
    direction = models.ForeignKey(
        SpecialtyDirection,
        null=True, blank=True,
        verbose_name='направление специальностей', on_delete=models.CASCADE)

    description = models.TextField('Описание', null=True, blank=True, )

    visible = models.BooleanField('Показывать?', default=True, db_index=True)

    what_study = models.TextField('Что изучают', null=True, blank=True)
    whom_work = models.TextField('Кем работают', null=True, blank=True)
    where_to_work = models.TextField('Где работать', null=True, blank=True)

    on_base = models.CharField('На базе', null=True,
                               blank=True, max_length=255)
    study_form = models.ForeignKey(StudyForm, null=True, blank=True,
        verbose_name='форма обучения', on_delete=models.CASCADE)

    training_period = models.CharField('Срок обучения', max_length=50, default='', db_index=True)

    max_average_point = models.IntegerField(
        'Максимальный средний балл',
        null=True, blank=True,
        db_index=True)

    min_average_point = models.IntegerField(
        'Минимальный средний балл',
        null=True, blank=True,
        db_index=True)

    qualifications = models.ForeignKey(
        Qualification,
        blank=True,
        null=True,
        verbose_name='Квалификации', on_delete=models.CASCADE)

    allobjects = models.Manager()
    objects = VisibleManager()

    def __str__(self):
        return '%s: %s' % (self.code, self.name)

    class Meta:
        ordering = ('name',)
        verbose_name = 'специальность'
        verbose_name_plural = 'специальности'


class Education(models.Model):
    """
    Модель образование в резюме
    """
    dateend = models.DateField("Дата окончание учебы")
    eduorg = models.ForeignKey(EduOrg, verbose_name="Образовательная организация", on_delete=models.CASCADE)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE)


class Employee(models.Model):
    """
    Модель резюме
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    edcations = models.ForeignKey(Education, on_delete=models.CASCADE)
    career = models.ForeignKey(Career, verbose_name="Карьера", blank=True, null=True, on_delete=models.CASCADE)
