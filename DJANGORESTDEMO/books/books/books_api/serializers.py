from rest_framework import serializers

from books.books_api.models import BookModel


class BookSerializer(serializers.ModelSerializer):
	def validate(self, attrs):
		if attrs.get("title"):
			if not attrs.get("title")[0].isupper():
				raise serializers.ValidationError("Title must be capitalized")
		return attrs

	class Meta:
		model = BookModel
		fields = '__all__'

