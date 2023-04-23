from django.urls import path

from templates_advanced.pythons_auth.views import login_view, logout_view, register_view

urlpatterns = [
	path('login/', login_view, name='login user'),
	path('logout/', logout_view, name='logout user'),
	path('register/', register_view, name='register user'),
]
