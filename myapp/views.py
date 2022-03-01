
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import City, Category, News
from .serializer import CitySerializer, CategorySerializer, NewsSerializer



class CityeAPIView(APIView):
    def get(self, request):
        cities = City.objects.all()
        serializer = CitySerializer(cities, many = True)
        return Response(data = serializer.data)
    
    def post(self, request):
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class CityDetailAPIView(APIView):
    def get(self, request, id):
        city = City.objects.get(id=id)
        serializer = CitySerializer(city)
        
        return Response(data=serializer.data)
    
    
class CategoryAPIView(APIView):

    def get(self, request):
        categoryes = Category.objects.all()
        serializer = CategorySerializer(categoryes, many = True)
        
        return Response(data=serializer.data)
    
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        
        
class CategoryDetailAPIView(APIView):
    def get(self,request, id):
        category = Category.objects.get(id = id)
        serializer = CategorySerializer(category)
        return Response(data=serializer.data)
    
    
class NewsAPIView(APIView):
    def get(self, request):
        news = News.objects.all()
        serializer = NewsSerializer(news, many = True )
        
        return Response(data=serializer.data)
            
    def post(self, request):
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        
        
        
        
        
        9