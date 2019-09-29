from django.contrib import admin
from .models import Profession, Region, Employee, Education, Specialty, EduOrg, TypeOrg
# Register your models here.

admin.site.register(Profession)
admin.site.register(Region)
admin.site.register(Employee)
admin.site.register(Specialty)
admin.site.register(Education)
admin.site.register(EduOrg)
admin.site.register(TypeOrg)