from rest_framework import serializers
from .models import Book, Author
from datetime import datetime

# Bookserializer that serializers all fields of the Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    
    # custom validation for publucation_year to ensure It's not in the future
    def validate_publication_year(self, value):
        if value > datetime.now().year:
            raise serializers.ValidationError("Publication year cannot be in the future")
        return value

# Author serializer that includes name field
class AuthorSerializer(serializers.ModelSerializer):
    # Nested BookSerializer to serialize the related books dynamically
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']