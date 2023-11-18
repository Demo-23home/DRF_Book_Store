from django.shortcuts import render
from .models import *
from .serializers import *
#Rest import 
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
# Create your views here.


@api_view(["GET"])
def list_book(request):
    books = Book.objects.all()  
    serializer = BookSerializer(books, many=True)  
    return Response(serializer.data)



@api_view(["GET"])
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    serializer = BookSerializer(book)
    return Response(serializer.data)


@api_view(["GET"])
def list_author(request):
    authors = Author.objects.all()  
    serializer = AuthorSerailizer(authors, many=True)  
    return Response(serializer.data)



@api_view(["GET"])
def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    serializer = AuthorSerailizer(author)
    return Response(serializer.data)