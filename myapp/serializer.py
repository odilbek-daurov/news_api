from rest_framework import serializers


from .models import City, Category, News

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['name', 'slug']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'slug']
        
        
class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'