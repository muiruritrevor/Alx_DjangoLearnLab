from django.db import models
from django.contrib.auth.models import User

    
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'blog_posts')

    def __str__(self):
        return self.title


# Create your models here.
