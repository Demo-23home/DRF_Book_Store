from rest_framework import serializers
from .models import *



class AuthorSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"




class ReviewSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    review_set = ReviewSerailizer(many=True)
    
    class Meta:
        model = Book
        fields = "__all__"
