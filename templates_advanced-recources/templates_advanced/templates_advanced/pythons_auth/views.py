from django.contrib.auth import logout, authenticate, login
from django.shortcuts import redirect


def login_view(request):
	username = 'donco'
	password = '12344qer'
	user = authenticate(username=username, password=password)
	if user:
		login(request, user)
	return redirect('index')


def logout_view(request):
	logout(request)
	return redirect('index')
