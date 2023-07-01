from rest_framework import serializers
from .models import BookModel,BookCategoryModel,AuthorModel
from django.shortcuts import get_object_or_404

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = ('firstname', 'lastname', 'year_born', 'nationality')

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = ('id','name','author','category','year_written')

class BookCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCategoryModel
        fields = ('name',)