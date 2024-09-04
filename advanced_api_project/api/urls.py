from django.urls import path
from .views import AuthorListCreateAPIView, BookListCreateAPIView

urlpatterns = [
    path('authors/', AuthorListCreateAPIView.as_view(), name='author-list-create'),
    path('books/', BookListCreateAPIView.as_view(), name='book-list-create'),
]
