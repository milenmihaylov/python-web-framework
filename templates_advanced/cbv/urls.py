from django.urls import path
from django.views.generic import TemplateView

from cbv import views

urlpatterns = [
	path('', views.IndexView.as_view(), name='cbv index'),
	path('2/', views.IndexTemplateView.as_view(), name='cbv index 2'),
	path('3/', TemplateView.as_view(template_name='cbv/index.html'), name='cbv index 3'),
	path('pets/', views.PetListView.as_view(), name='cbv pets'),
	path('details/<int:pk>', views.PetDetailsView.as_view(), name='cbv pet details'),
	path('create/', views.PetCreateView.as_view(), name='cbv create pet'),
]
