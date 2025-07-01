from django.urls import path

from apps.library.views import *

urlpatterns = [
    path("authors/", AuthorListCreateView.as_view()),
    path("authors/<int:pk>/", AuthorDEtailView.as_view()),
    path("books/", BookListCreateView.as_view()),
    path("books/<int:pk>/", BookDEtailView.as_view())
]
