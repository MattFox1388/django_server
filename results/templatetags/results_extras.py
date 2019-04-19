from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def dateToISO(str):
    datetime_parts = str.split(' ')
    return datetime_parts[0]

@register.filter
def to_int(val):
    return int(val)

