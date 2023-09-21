from django.urls import path

from async_and_celery.web.views import index, index_slow, transcribe

urlpatterns = [
	path('', index, name='index'),
	path('slow/', index_slow, name='index slow'),
	path('transcribe/<int:pk>/', transcribe, name='transcribe'),
]
