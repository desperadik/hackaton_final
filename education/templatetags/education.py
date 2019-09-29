# -*- coding: utf-8 -*-

from education.models import Profession
from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def get_professions(context):
    return Profession.objects.all()
