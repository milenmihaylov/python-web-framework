from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView

from cats.common.form_mixins import BootstrapFormViewMixin
from cats.web.models import Cat


def index(request):
	context = {
		'title': 'Hello from FBV!',
	}
	return render(request, 'index.html', context)


class IndexView(TemplateView):
	template_name = 'index.html'

	def get_context_data(self, **kwargs):
		return {
			'title': 'Hello from CBV!',
		}


def show_cats(request):
	context = {
		'cats': Cat.objects.all(),
		'cats_title': 'Hello FBV Cats!',
	}
	return render(request, 'cats-list.html', context)


class ShowCatsListView(ListView):
	model = Cat
	template_name = 'cats-list.html'
	context_object_name = 'cats'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		context['cats_title'] = 'Hello CBV cats!'
		return context


class CatCreateView(BootstrapFormViewMixin, CreateView):
	model = Cat
	template_name = 'create-cat.html'
	fields = '__all__'
	success_url = reverse_lazy('cbv show cats')



