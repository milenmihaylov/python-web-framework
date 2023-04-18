from os.path import join, isfile

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect

from resources.forms import PetForm
from resources.models import Pet


def pets(request):
	if request.method == 'GET':
		context = {
			'form': PetForm(),
			'pets': Pet.objects.all()
		}
		return render(request, 'resources/pets_index.html', context)
	else:
		form = PetForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('pets')
		context = {
			'form': form,
			'pets': Pet.objects.all(),
		}
		return render(request, 'resources/pets_index.html', context)


def get_private_file(request, path_to_file):
	full_path = join(settings.MEDIA_ROOT, 'private', path_to_file)
	if isfile(full_path):
		file = open(full_path, 'rb')
		response = HttpResponse(content=file)
		response['Content-Dispostion'] = 'attachment'
		return response
