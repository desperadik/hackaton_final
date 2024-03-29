# Generated by Django 2.2.5 on 2019-09-28 16:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('region', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateend', models.DateField(verbose_name='Дата окончание учебы')),
            ],
        ),
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to='', verbose_name='Картинка')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('short_description', models.CharField(blank=True, max_length=150, null=True, verbose_name='Краткое описание')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'профессия',
                'verbose_name_plural': 'профессии',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ProfessionGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, null=True, verbose_name='Slug')),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='Название')),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to='', verbose_name='Картинка')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'группа профессий',
                'verbose_name_plural': 'Группы профессий',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='Название')),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to='', verbose_name='Картинка')),
                ('short_preview', models.TextField(blank=True, max_length=355, null=True, verbose_name='Краткое описание')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('order_index', models.DecimalField(blank=True, db_index=True, decimal_places=0, default=0, max_digits=2, verbose_name='Порядок')),
                ('pluse', models.TextField(blank=True, null=True, verbose_name='Плюсы')),
                ('cons', models.TextField(blank=True, null=True, verbose_name='Минусы')),
                ('description_end', models.TextField(blank=True, null=True, verbose_name='Описание2')),
                ('slug', models.SlugField(blank=True, null=True, verbose_name='Slug')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
            ],
            options={
                'verbose_name': 'квалификация',
                'verbose_name_plural': 'квалификации',
                'ordering': ['order_index'],
            },
        ),
        migrations.CreateModel(
            name='SpecialtyGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, null=True, verbose_name='Slug')),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='Название')),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to='', verbose_name='Картинка')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'группа специальностей',
                'verbose_name_plural': 'группы специальностей',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='StudyForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'форма обучения',
                'verbose_name_plural': 'формы обучения',
            },
        ),
        migrations.CreateModel(
            name='TypeOrg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Например:  Технический, Гуманитарный и тп', max_length=100, verbose_name='Тип обрахзовательной организации')),
            ],
        ),
        migrations.CreateModel(
            name='SpecialtyDirection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='Название')),
                ('code', models.CharField(db_index=True, max_length=10, verbose_name='Код направления')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='education.SpecialtyGroup', verbose_name='Группа специальностей')),
            ],
            options={
                'verbose_name': 'направление специальностей',
                'verbose_name_plural': 'направления специальностей',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover', models.ImageField(upload_to='', verbose_name='image')),
                ('code', models.CharField(db_index=True, max_length=10, verbose_name='Код специальности')),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='Название')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('visible', models.BooleanField(db_index=True, default=True, verbose_name='Показывать?')),
                ('what_study', models.TextField(blank=True, null=True, verbose_name='Что изучают')),
                ('whom_work', models.TextField(blank=True, null=True, verbose_name='Кем работают')),
                ('where_to_work', models.TextField(blank=True, null=True, verbose_name='Где работать')),
                ('on_base', models.CharField(blank=True, max_length=255, null=True, verbose_name='На базе')),
                ('training_period', models.CharField(db_index=True, default='', max_length=50, verbose_name='Срок обучения')),
                ('max_average_point', models.IntegerField(blank=True, db_index=True, null=True, verbose_name='Максимальный средний балл')),
                ('min_average_point', models.IntegerField(blank=True, db_index=True, null=True, verbose_name='Минимальный средний балл')),
                ('direction', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='education.SpecialtyDirection', verbose_name='направление специальностей')),
                ('professions', models.ManyToManyField(blank=True, to='education.Profession', verbose_name='Профессии')),
                ('qualifications', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='education.Qualification', verbose_name='Квалификации')),
                ('study_form', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='education.StudyForm', verbose_name='форма обучения')),
            ],
            options={
                'verbose_name': 'специальность',
                'verbose_name_plural': 'специальности',
                'ordering': ('name',),
            },
            managers=[
                ('allobjects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='profession',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='professions', to='education.ProfessionGroup', verbose_name='группа профессий'),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edcations', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='education.Education')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='region.Region')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EduOrg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('inn', models.CharField(max_length=16, verbose_name='ИНН')),
                ('desc', models.TextField(verbose_name='Описание')),
                ('typeorg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='education.TypeOrg')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='education',
            name='eduorg',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='education.EduOrg', verbose_name='Образовательная организация'),
        ),
        migrations.AddField(
            model_name='education',
            name='specialty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='education.Specialty'),
        ),
    ]
