from django.shortcuts import render, redirect

from templates_advanced.profiles.forms import ProfileForm
from templates_advanced.profiles.models import Profile


def profile_details(request):
	user_id = request.user.id
	profile = Profile.objects.get(pk=user_id)
	if request.method == 'POST':
		form = ProfileForm(request.POST, instance=profile)
		if form.is_valid():
			form.save()
			return redirect('index')
	else:
		form = ProfileForm(instance=profile)

	context = {
		'form': form
	}
	return render(request, 'profile_detail.html', context)
