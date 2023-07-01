from django.urls import path
from .views import (DetailBookView, AllBookView,CreateBookView,
                    DeleteBookView,UpdateBookView)
urlpatterns = [
    path('', AllBookView.as_view()),
    path('/<int:book_id>/', DetailBookView.as_view()), #be careful with the 'book_id'
    path('/create/', CreateBookView.as_view()),
    path('/update/<int:book_id>/',UpdateBookView.as_view()),
    path('/delete/<int:book_id>/',DeleteBookView.as_view()),
]