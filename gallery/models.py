from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class CuratorProfile(models.Model):
    user_account = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    biography = models.TextField(max_length=500, blank=True)
    avatar = models.FileField(upload_to='avatars/', default='avatars/default.png', blank=True)

class CategoryTag(models.Model):
    name = models.CharField(max_length=50, unique=True)

class Artwork(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image_file = models.FileField(upload_to='monolith_art/')
    created_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='artworks')
    tags = models.ManyToManyField(CategoryTag, related_name='artworks', blank=True)
    favorites = models.ManyToManyField(User, related_name='favorited_artworks', blank=True)
    likes = models.ManyToManyField(User, related_name='liked_artworks', blank=True)

    def total_likes(self):
        return self.likes.count()