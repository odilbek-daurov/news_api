from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import CategoryAPIView, CategoryDetailAPIView, CityeAPIView,CityDetailAPIView, NewsModelViewSet

router = DefaultRouter()
router.register('news', NewsModelViewSet)
urlpatterns = [
    path('city/', CityeAPIView.as_view(), name='city'),
    path('city/<int:id>', CityDetailAPIView.as_view(), name='city_detail'),
    path('category/', CategoryAPIView.as_view(), name='category'),
    path('category/<int:pk>', CategoryDetailAPIView.as_view(), name='category_detail'),
    path('', include(router.urls)),
]
