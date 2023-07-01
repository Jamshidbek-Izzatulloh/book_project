from django.db import models
from datetime import datetime


class AuthorModel(models.Model):
    name = models.CharField(max_length=100, default='Not Given')
    year_born = models.DateField(default='Not given')
    nationality = models.CharField(max_length=50, default='Not Given')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'author'


class BookCategoryModel(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'book_category'

class BookModel(models.Model):
    name = models.CharField(max_length=50, default='')
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE)
    category = models.ForeignKey(BookCategoryModel, on_delete=models.CASCADE)
    year_written = models.PositiveIntegerField(default=datetime.now)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'book'
