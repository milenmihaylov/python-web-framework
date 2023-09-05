from django.urls import path

from to_deploy.app.views import RegisterView, LoginUser, IndexView

urlpatterns = [
	path('register/', RegisterView.as_view(), name='register_user'),
	path('login/', LoginUser.as_view(), name='login_user'),
	path('', IndexView.as_view(), name='home'),
]
