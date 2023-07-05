from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import BookModel
from .serializers import BookSerializer
from rest_framework import status
from rest_framework import generics

class AllCreateBookView(generics.ListCreateAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
    
class ReadUpdateDeleteBookView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
