from django.urls import path

from apps.library.views import *

# urlpatterns = [
#     path("authors/", AuthorListAPIView.as_view(), name="author-list"),
#     path("authors/create/", AuthorCreateAPIView.as_view(), name='create-author'),
#     path("authors/<int:pk>/", AuthorRetrieveAPIView.as_view(), name='detail-authors'),
#     path("authors/<int:pk>/update/", AuthorUpdateAPIView.as_view(), name='update-author'),
#     path("authors/<int:pk>/dalete/", AuthorDeleteAPIView.as_view(), name='delete-author'),
# 
#     path("books/", BooksListAPiView.as_view(), name="Books-list"),
#     path("books/create/", BooksCreateAPiView.as_view(), name='create-Books'),
#     path("books/<int:pk>/", BooksRetrieveAPiView.as_view(), name='detail-books'),
#     path("books/<int:pk>/update/", BooksUpdateAPiView.as_view(), name='update-Books'),
#     path("books/<int:pk>/dalete/", BooksDeleteAPiView.as_view(), name='delete-Books'),
# ]