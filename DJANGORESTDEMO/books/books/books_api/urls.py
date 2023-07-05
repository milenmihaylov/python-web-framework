from django.urls import path

from books.books_api import views

urlpatterns = [
	path('', views.BookListCreate.as_view(), name=''),
	path('<int:book_id>', views.BookGetUpdateDelete.as_view()),
]
