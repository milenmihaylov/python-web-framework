from django.http import HttpResponse


def group_required(groups: list):
	required_groups_set = set(groups)

	def decorator(view_func):
		def wrapper(request, *args, **kwargs):
			user_groups_set = set(group.name for group in request.user.groups.all())
			if required_groups_set.intersection(user_groups_set) or \
				request.user.is_superuser:
				return view_func(request, *args, **kwargs)
			else:
				return HttpResponse('Authorization required', status=401)

		return wrapper

	return decorator
