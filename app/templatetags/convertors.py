from django import template

register = template.Library()


@register.filter
def str_to_float(value):
    try:
        return float(value)
    except ValueError as e:
        return None
