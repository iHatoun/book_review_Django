from rest_framework import serializers
from .models import Book, Review
from django.contrib.auth.models import User

# سيريالايزر لكتاب
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'description']

# سيريالايزر لمراجعة
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'book', 'user', 'rating', 'comment', 'created_at']
        read_only_fields = ['user', 'created_at']

# سيريالايزر للمستخدم (للتسجيل وتغيير كلمة المرور)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
