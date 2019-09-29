# -*- coding: utf-8 -*-

from education.models import Profession, Specialty
from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def get_professions(context):
    return Profession.objects.all()

@register.simple_tag(takes_context=True)
def get_specialites(context):
    return Specialty.allobjects.all()