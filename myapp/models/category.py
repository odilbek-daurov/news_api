from django.db import models
from django.core.exceptions import ValidationError


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    
    def __str__(self) -> str:
        return self.name
    

    def validate_name(value):
        if len(value) <= 2:
            raise ValidationError('categoriya kamida 2 ta belgidan iborat bo`lishi kerek')