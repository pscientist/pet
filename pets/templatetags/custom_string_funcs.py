from django import template

register = template.Library()

@register.filter
def newline(s):
    return s.replace('\n', '<br/>')
