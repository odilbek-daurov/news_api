from django.urls import path

from .views import CategoryAPIView, CategoryDetailAPIView, CityeAPIView,CityDetailAPIView, NewsAPIView

urlpatterns = [
    path('city/', CityeAPIView.as_view(), name='city'),
    path('city/<int:id>', CityDetailAPIView.as_view(), name='city_detail'),
    path('category/', CategoryAPIView.as_view(), name='category'),
    path('category/<int:id>', CategoryDetailAPIView.as_view(), name='category_detail'),
    path('news/', NewsAPIView.as_view(), name='news'),
]
