from django.urls import path, include
from .views import BookList
from api import views

urlpatterns = [
    path("api/books", BookList.as_view(), name="book_list"),
]



# from rest_framework.routers import DefaultRouter
# from .views import BookViewSet
# from django.urls import path, include

# router = DefaultRouter()
# router.register(r'books', BookViewSet)

# urlpatterns = router.urls