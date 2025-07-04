from rest_framework import serializers
from apps.library.models import Book, Author
import datetime

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source="author.name", read_only=True)
    
    class Meta:
        model = Book
        fields = "__all__"

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidateError("Цена должно быть больше 0!")
        return values


    def validate_year(self, value):
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidateError(f"Год не может быть больше {current_year}")
        return value
