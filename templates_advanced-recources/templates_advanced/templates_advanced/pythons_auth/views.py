from django.contrib.auth import logout, login, get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from templates_advanced.pythons_auth.forms import LogInForm, RegisterForm
from templates_advanced.pythons_auth.mixins import BootstrapRegisterMixin


USER_MODEL = get_user_model()

# def register_view(request):
# 	if request.method == 'POST':
# 		form = RegisterForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			return login_view(request)
# 		context = {
# 			'form': form,
# 			'register': True,
# 		}
# 		return render(request, 'auth/register_or_login.html', context)
# 	else:
# 		context = {
# 			'form': RegisterForm(),
# 			'register': True,
# 		}
# 		return render(request, 'auth/register_or_login.html', context)


# def login_view(request):
# 	if request.method == 'POST':
# 		form = LogInForm(request.POST)
# 		if form.is_valid():
# 			user = form.save()
# 			login(request, user)
# 			return redirect('index')
# 	else:
# 		form = LogInForm()
#
# 	context = {
# 		'form': form
# 	}
# 	return render(request, 'auth/register_or_login.html', context)


class LogInView(LoginView):
	template_name = 'auth/register_or_login.html'
	form_class = LogInForm

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['register'] = False
		return context

	def get_success_url(self):
		return reverse('index')


# fa


class LogOutView(LogoutView):
	next_page = reverse_lazy('index')


class RegisterView(BootstrapRegisterMixin, CreateView):
	model = USER_MODEL
	form_class = RegisterForm
	template_name = 'auth/register_or_login.html'
	success_url = reverse_lazy('login user')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['register'] = True
		return context
