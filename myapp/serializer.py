from rest_framework import serializers
from django.core.exceptions import ValidationError


from .models import City, Category, News

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['name', 'slug']

    def validate_name(self, value):
        if len(value)<3:
            raise ValidationError('categoriya kamida 2 ta belgidan iborat bo`lishi kerek')
        return value

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'slug']
        
    def validate_name(self, value):
        if len(value) <= 2:
            raise ValidationError('categoriya kamida 2 ta belgidan iborat bo`lishi kerek')
        return value
        
        
class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'title', 'slug', 'content', 'image', 'image', 'views', 'city', 'category']
        
    def validate_content(self, value):
        s = len(list(value.split()))
        if s < 1:
            raise ValidationError('news kamida 4 ta belgidan iborat bo`lishi kerek')
        return value

    def validate_image(self, value):
        s = value[-4:]
        if '.jpg' != s or '.png' != s:
            raise ValidationError('rasm jpg yoki png formatda bo`lishi kerak bo`lishi kk')
        return value
    # def validated_data(self):