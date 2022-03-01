from django.db import models

class City(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    
    def __str__(self) -> str:
        return self.name