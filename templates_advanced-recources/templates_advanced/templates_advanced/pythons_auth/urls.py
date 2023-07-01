from django.urls import path

from templates_advanced.pythons_auth.views import RegisterView, LogInView, LogOutView

urlpatterns = [
	# path('login/', login_view, name='login user'),
	path('login/', LogInView.as_view(), name='login user'),
	# path('logout/', logout_view, name='logout user'),
	path('logout/', LogOutView.as_view(), name='logout user'),
	# path('register/', register_view, name='register user'),
	path('register/', RegisterView.as_view(), name='register user'),
]
