from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from resources.models import Pet


class IndexView(View):
	def get(self, request):
		context = {
			'title': 'Hello form Index CBV',
			'pets': Pet.objects.all(),
		}
		return render(request, 'cbv/index.html', context)

	def post(self, request):
		pass


class IndexTemplateView(TemplateView):
	template_name = 'cbv/index.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Hello form TemplateView'
		context['pets'] = Pet.objects.all()
		return context


class PetListView(ListView):
	template_name = 'cbv/index.html'
	model = Pet
	context_object_name = 'pets'
	paginate_by = 2

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Hello form ListView'
		return context

	def dispatch(self, request, *args, **kwargs):
		if 'page_size' in request.GET:
			self.paginate_by = request.GET['page_size']
		return super().dispatch(request, *args, **kwargs)


class PetDetailsView(DetailView):
	template_name = 'cbv/details.html'
	model = Pet
	context_object_name = 'pet'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)  # here we should use super() because we'll lose the model context
		pet = context['pet']
		context['title'] = f'{pet.name}\'s details'
		return context




class PetCreateView(CreateView):
	model = Pet
	template_name = 'cbv/create-pet.html'
	fields = '__all__'
	success_url = reverse_lazy('cbv index')
