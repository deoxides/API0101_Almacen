from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='display')
@stringfilter
def cut(value,arg):
    return value[arg]