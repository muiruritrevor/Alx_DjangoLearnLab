from django.urls import path
from .views import LoginView, LogoutView, RegisterView, list_books, admin_view, librarian_view, member_view, add_book, edit_book, delete_book, LibraryDetailView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('books/', list_books, name='book_list'),
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
    path('book/add/', add_book, name='add_book'),
    path('book/edit/<int:pk>/', edit_book, name='edit_book'),
    path('book/delete/<int:pk>/', delete_book, name='delete_book'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
