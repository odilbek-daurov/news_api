from django.test import Client, TestCase



class TestCategoryAPIView(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        
    def test_category_url(self):
        res = self.client.get('/category')

        self.assertEqual(res.status_code, 301)