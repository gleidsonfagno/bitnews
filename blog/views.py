# from django.shortcuts import render
# from django.contrib.auth.models import User
# from rest_framework import serializers, viewsets, permissions
# from rest_framework.response import Response
# from rest_framework.decorators import action
# from rest_framework.routers import DefaultRouter
# from django.urls import path, include

# Create your views here.
# class CategoriaViewSet(viewsets.ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategoriaSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     permission_classes = [permissions.IsAuthenticated]

#     def get_serializer_class(self):
#         if self.action in ['create', 'update', 'partial_update']:
#             return PostCreateUpdateSerializer
#         return PostSerializer

#     def perform_create(self, serializer):
#         serializer.save(autor=self.request.user)

#     @action(detail=True, methods=['get'], permission_classes=[permissions.AllowAny])
#     def categoria(self, request, pk=None):
#         categoria = self.get_object()
#         posts = Post.objects.filter(categoria=categoria)
#         serializer = self.get_serializer(posts, many=True)
#         return Response(serializer.data)

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