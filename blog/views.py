
from rest_framework import generics
from rest_framework.views import APIView
from .models import Category, Post
from .serializers import CategorySerializer, PostSerializer
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator


class HomeView(APIView):
    @method_decorator(cache_page(60 * 15))
    def get(self, request):
        data = {
            "message": "Bem-vindo à API do BitNews",
            "available_routes": {
                "categories": "/api/categories/",
                "posts": "/api/posts/",
            },
        }
        return Response(data, status=status.HTTP_200_OK)

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer