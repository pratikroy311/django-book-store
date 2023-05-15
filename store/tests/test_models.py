from django.test import TestCase

from store import models

class TestCategoriesModel(TestCase):

    def setup(self):
        self.data1 = models.Category.objects.create(name='django',\
                                                    slug='django')
        
    def test_category_model_entry(self):
        data = self.data1
        self.assertTrue(isinstance(data,models.Category))

    def test_category_model_entry(self):
        data = self.data1
        self.assertEqual(str(data),'django')