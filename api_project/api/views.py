from rest_framework import generics, viewsets
from .serializers import BookSerializer
from .models import Book

# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# using cbv
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# # using Fbv
# @api_view(['GET'])
# def book_list(request):
#     books = Book.objects.all()
#     serializer = BookSerializer(books, many = True)
#     return Response(serializer.data)


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    #Permissions_class = ([])


# from django.shortcuts import render
# from rest_framework import generics, viewsets
# from .models import Book 
# from .serializers import BookSerializer
# from rest_framework.permissions import IsAuthenticated

# class BookList(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# class BookViewSet(viewsets.ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [IsAuthenticated]



# # Create your views here.
