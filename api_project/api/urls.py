from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet
from api import views

router = DefaultRouter()
router.register(r'books', BookViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path("api/books", BookList.as_view(), name="book_list"),
    # path("api/books", BookList, name='book_list') // FBV url
]



# from rest_framework.routers import DefaultRouter
# from .views import BookViewSet
# from django.urls import path, include

# router = DefaultRouter()
# router.register(r'books', BookViewSet)

# urlpatterns = router.urls