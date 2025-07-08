# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
# from rest_framework import status
# from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import filters 
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, mixins

from apps.library.models import Book, Author
from apps.library.serializers import BookSerializer, AuthorSerializer


class AuthorAPI(viewsets.GenericViewSet,
                mixins.ListModelMixin,
                mixins.CreateModelMixin,
                mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookAPI(viewsets.GenericViewSet,
                mixins.CreateModelMixin,
                mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

@method_decorator(cache_page(60), name='dispatch')
class BookListAPI(viewsets.GenericViewSet,
                   mixins.ListModelMixin):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['year', 'price', 'author']
    search_fields = ['title', 'author__name']
    ordering_fields = ['year', 'price']


# class AuthorListAPIView(ListAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
# 
# class AuthorCreateAPIView(CreateAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
# 
# class AuthorRetrieveAPIView(RetrieveAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
# 
# class AuthorUpdateAPIView(UpdateAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
# 
# class AuthorDeleteAPIView(DestroyAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
# 
# @method_decorator(cache_page(60), name='dispatch')
# class BooksListAPiView(ListAPIView):
#     queryset = Book.objects.select_related("author").all()
#     serializer_class = BookSerializer
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
#     filterset_fields = ['year', 'price', 'author']
#     search_fields = ['title', 'author__name']
#     ordering_fields = ['year', 'price']
# 
# class BooksCreateAPiView(CreateAPIView):
#     queryset = Book.objects.select_related("author").all()
#     serializer_class = BookSerializer
# 
# class BooksRetrieveAPiView(RetrieveAPIView):
#     queryset = Book.objects.select_related("author").all()
#     serializer_class = BookSerializer
# 
# class BooksUpdateAPiView(UpdateAPIView):
#     queryset = Book.objects.select_related("author").all()
#     serializer_class = BookSerializer
# 
# class BooksDeleteAPiView(DestroyAPIView):
#     queryset = Book.objects.select_related("author").all()
#     serializer_class = BookSerializer