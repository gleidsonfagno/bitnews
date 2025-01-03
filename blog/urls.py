from django.urls import path
from .views import CategoryListCreateView, CategoryDetailView , PostListCreateView, PostDetailView , HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),  # Rota inicial para a visão geral
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
]
