from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)
    category_image =models.ImageField(upload_to="category_images", blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    resume = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="post_images", blank=True, null=True)
    categoria = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    # autor = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    like = models.FloatField(default=0)  # Inicializa com 0, pode ser alterado para incrementar os likes
    views = models.IntegerField(default=0)  # Quantidade de visualizações
    status = models.CharField(max_length=20, choices=[('draft', 'Draft'), ('published', 'Published')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
