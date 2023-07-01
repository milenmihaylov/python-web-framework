from django.urls import path

from templates_advanced.profiles.views import ProfileDetailsView, profile_details

urlpatterns = [
	# path('<slug:slug>/', ProfileDetailsView.as_view(), name='profile details'),
	path('', profile_details, name='profile details'),
]

import templates_advanced.profiles.signals
