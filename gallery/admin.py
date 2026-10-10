from django.contrib import admin
from .models import Artwork, CategoryTag, CuratorProfile

# Register your models here.
admin.site.register(Artwork)
admin.site.register(CategoryTag)
admin.site.register(CuratorProfile)