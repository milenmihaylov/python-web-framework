from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import PythonCreateForm
from .models import Python
from ..python_core.decorators import group_required


def index(req):
	pythons = Python.objects.all()
	return render(req, 'index.html', {'pythons': pythons})


# @login_required(login_url='login user')
@group_required(groups=['Regular user'])
def create(req):
	if req.method == 'GET':
		form = PythonCreateForm()
		return render(req, 'create.html', {'form': form})
	else:
		data = req.POST, req.FILES
		form = PythonCreateForm(*data)
		if form.is_valid():
			python = form.save()
			python.save()
			return redirect('index')
