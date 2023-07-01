from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, CreateView

from .forms import PythonCreateForm
from .mixins import BootstrapFormViewMixin, GroupRequiredMixin
from .models import Python
from ..python_core.decorators import group_required


# def index(req):
# 	pythons = Python.objects.all()
# 	return render(req, 'index.html', {'pythons': pythons})


class IndexView(ListView):
	model = Python
	template_name = 'index.html'
	context_object_name = 'pythons'
	paginate_by = 6


# @login_required()
# # @group_required(groups=[])
# def create(req):
# 	if req.method == 'GET':
# 		form = PythonCreateForm()
# 		return render(req, 'create_python.html', {'form': form})
# 	else:
# 		data = req.POST, req.FILES
# 		form = PythonCreateForm(*data)
# 		if form.is_valid():
# 			python = form.save()
# 			python.save()
# 			return redirect('index')


class CreatePythonView(BootstrapFormViewMixin, GroupRequiredMixin, CreateView):
	model = Python
	fields = '__all__'
	template_name = 'create_python.html'
	success_url = reverse_lazy('index')
