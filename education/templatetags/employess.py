# -*- coding: utf-8 -*-

from education.models import Profession, Employee
from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def get_employees(context):
    return Employee.objects.all()
