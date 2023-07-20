from django import template

register = template.Library()


@register.filter
def object_type(obj):
    return type(obj).__name__
