from django import template

register = template.Library()


@register.filter()
def capitalize(value: str, capitalize_chars_count=1):
	return value[:capitalize_chars_count].upper() + value[capitalize_chars_count:].lower()
