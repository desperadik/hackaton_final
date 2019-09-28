from django.contrib import admin

# Register your models here.
from django.db.models import Count

from vacancy.models import Vacancy, Category, Profession


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ['category','profession', 'title', 'salary', 'company']
    list_filter = ['category']


class VacancyInLine(admin.StackedInline):
    model = Vacancy
    fields = ['title']
    # readonly_fields = True


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'cnt_vacancy', 'code']
    search_fields = ['code']


@admin.register(Profession)
class ProfessionAdmin(admin.ModelAdmin):
    list_display = ['name', 'show_vacancy_count']
    inlines = [VacancyInLine,]


    def get_queryset(self, request):
        qs = super(ProfessionAdmin, self).get_queryset(request)
        # The query have to return multiple annotation, for this use distinct=True in the Count function
        qs = qs.annotate(cnt_vacancy=Count('vacancy', distinct=True))
        return qs

    def show_vacancy_count(self, inst):
        return inst.cnt_vacancy

    show_vacancy_count.admin_order_field = 'cnt_vacancy'