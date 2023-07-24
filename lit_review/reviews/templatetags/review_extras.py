from django import template

register = template.Library()


@register.filter
def object_type(obj):
    return type(obj).__name__


@register.filter
def stars(number, max_star=5):
    """★☆"""
    return f"{number*'★'}{(max_star-number)*'☆'}"
