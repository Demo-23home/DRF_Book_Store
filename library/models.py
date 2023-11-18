from django.db import models
from django.core.validators import  MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=100, default="")
    birth_date = models.CharField(max_length=50, default="")
    bio = models.TextField(default="")

    def __str__(self):
        return self.name
    


class Book(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    publication_date = models.DateField(auto_now=False, auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    


class Review(models.Model):
    reviewer_name = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(default="")
    rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    book = models.ManyToManyField(Book)

    def __str__(self):
        return f"{self.reviewer_name}"
    


