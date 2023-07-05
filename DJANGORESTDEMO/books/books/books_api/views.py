from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from books.books_api.models import BookModel
from books.books_api.serializers import BookSerializer


class BookListCreate(APIView):

	def get(self, request):
		books = BookModel.objects.all()
		serializer = BookSerializer(books, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = BookSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(data=serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookGetUpdateDelete(APIView):
	def put(self, request, book_id):
		try:
			book = BookModel.objects.get(id=book_id)
			serializer = BookSerializer(instance=book, data=request.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data)
			return Response(serializer.errors)
		except:
			return Response({'message': 'Not <<<<<<<<<<found'}, status=status.HTTP_404_NOT_FOUND)

	def get(self, request, book_id):
		try:
			book = BookModel.objects.get(id=book_id)
			serializer = BookSerializer(book)
			return Response(data=serializer.data)
		except:
			return Response({'message': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)

	def delete(self, request, book_id):
		try:
			book = BookModel.objects.get(id=book_id)
			book.delete()
			return Response(status=status.HTTP_200_OK)
		except:
			return Response({'message': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
