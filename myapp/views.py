from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework import status, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import City, Category, News
from .serializer import CitySerializer, CategorySerializer, NewsSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from  rest_framework.pagination import LimitOffsetPagination



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
    
    def put(self, request, id):
        city = City.objects.get(id = id)
        serializer = CitySerializer(city, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        city = City.objects.get(id = id)
        city.delete()
        return Response(status=status.HTTP_204_NOT_FOUND)
    
class CategoryAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
        
        
class CategoryDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class NewsModelViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = LimitOffsetPagination

    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.SearchFilter,  filters.OrderingFilter]
    ordering_fields = ['views']
    search_fields = ['title', 'content', 'city__name']
    
    @action(detail=True, methods=['get'])
    def views_count(self, request, pk):
        new = self.get_object()
        serializer = NewsSerializer(new)
        new.views += 1
        new.save()

        return Response(serializer.data)

        
        