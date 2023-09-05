from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, CreateView


class RegisterView(CreateView):
	template_name = 'accounts/register.html'
	form_class = UserCreationForm
	success_url = reverse_lazy('home')

	def form_valid(self, form):
		form = super().form_valid(form)
		login(self.request, self.object)  # TODO: add to bookworm
		return form


class LoginUser(LoginView):
	template_name = 'accounts/login.html'
	success_url = reverse_lazy('home')


class IndexView(TemplateView):
	template_name = 'web/index.html'
