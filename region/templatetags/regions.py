# -*- coding: utf-8 -*-

from region.models import Region
from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def get_regions(context):
    return Region.objects.all()
