class BootstrapFormViewMixin:
	@staticmethod
	def __apply_bootstrap_class(form):
		for (_, field) in form.fields.items():
			field.widget.attrs = {
				'class': 'form-control',
			}

	def get_form(self, **kwargs):
		form = super().get_form(**kwargs)
		self.__apply_bootstrap_class(form)
		return form
