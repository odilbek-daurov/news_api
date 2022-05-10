
from django.test import TestCase

from myapp.serializer import CategorySerializer, NewsSerializer
from myapp.models import Category, News

class TestCategorySerial(TestCase):
    def setUp(self):
        self.fan = Category.objects.create(name='Fann', slug='fann')
        
        
    def test_data(self):
        self.data = CategorySerializer(self.fan).data
        assert self.data['name'] == 'Fann'
        # assert data['id'] is not None
            
            
    def test_valid_name(self):
        self.texnika = {
            'name':'Tex',
            'slug':'texksksk'
        } 
        self.data1 = CategorySerializer(data = self.texnika)
        self.assertTrue(self.data1.is_valid)


class TestSerializerNews(TestCase):
    def setUp(self):
        self.news1 = News.objects.create(
            title='Kun yangiligi',
            slug='kunyangiligi',
            content='bugun kun yomg`irli',
            image='http://jsjsjjs.jpg',
            # category_id=1,
        )

    def test_data(self):
        self.data = NewsSerializer(self.news1).data
        assert self.data['title'] == 'Kun yangiligi'
