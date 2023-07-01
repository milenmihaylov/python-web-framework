from django.core.exceptions import PermissionDenied


class BootstrapFormViewMixin:
	@staticmethod
	def __apply_bootstrap_class(form):
		form.fields['name'].widget.attrs = {'class': 'form-control'}
		form.fields['description'].widget.attrs = {'class': 'form-control', 'rows': '3'}
		form.fields['image'].widget.attrs = {'class': 'custom-file'}

	def get_form(self, **kwargs):
		form = super().get_form(**kwargs)
		self.__apply_bootstrap_class(form)
		return form


class GroupRequiredMixin:
	"""
		group required - list of strings, required param
	"""

	group_required = ['User']

	def dispatch(self, request, *args, **kwargs):
		if request.user.is_superuser:
			return super().dispatch(request, *args, **kwargs)

		if not request.user.is_authenticated:
			raise PermissionDenied

		user_group_names = [g.name for g in request.user.groups.all()]
		result = set(user_group_names).intersection(self.group_required)
		if self.group_required and not result:
			raise PermissionDenied

		return super(GroupRequiredMixin, self).dispatch(request, *args, **kwargs)
