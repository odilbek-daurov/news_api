from django.db import models

from .city import City
from .category import Category



class News(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    content = models.TextField()
    image = models.URLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,blank=True, null=True)
    
    def __str__(self) -> str:
        return self.title