from django.urls import path
from .views import (ReadUpdateDeleteBookView, AllCreateBookView,)
urlpatterns = [
    path('', AllCreateBookView.as_view()),
    path('<pk>/', ReadUpdateDeleteBookView.as_view()),
    # path('<pk>/', DetailBookView.as_view()), #be careful with the 'book_id'
    # path('create/', CreateBookView.as_view()),
    # path('update/<pk>/',UpdateBookView.as_view()),
    # path('delete/<pk>/',DeleteBookView.as_view()),
]