from django.contrib.auth import logout, login
from django.shortcuts import redirect, render

from templates_advanced.pythons_auth.forms import LogInForm, RegisterForm


def register_view(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			return login_view(request)
		context = {
			'form': form,
			'register': True,
		}
		return render(request, 'auth/register_or_login.html', context)
	else:
		context = {
			'form': RegisterForm(),
			'register': True,
		}
		return render(request, 'auth/register_or_login.html', context)


def login_view(request):
	if request.method == 'POST':
		form = LogInForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect('index')
	else:
		form = LogInForm()

	context = {
		'form': form
	}
	return render(request, 'auth/register_or_login.html', context)


def logout_view(request):
	logout(request)
	return redirect('index')
