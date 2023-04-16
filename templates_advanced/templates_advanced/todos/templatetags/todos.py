from django import template

from templates_advanced.todos.models import Todo

register = template.Library()


@register.simple_tag()
def todos_count():
	return Todo.objects.all().count()
