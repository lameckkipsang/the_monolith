from django.db import models

# Create your models here.
class CategoryTag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self): return f"#{self.name}"

class Artwork(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image_file = models.FileField(upload_to='monolith_art/')
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(CategoryTag, related_name='artworks', blank=True)
    
    def __str__(self): return self.title