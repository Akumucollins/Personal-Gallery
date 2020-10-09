from django.test import TestCase
from .models import Image

class TestImage(TestCase):
    def setUp(self):
        self.image_pic = Image(id=1, name='image', description='This is photo gallery test')

    def test_instance(self):
        self.assertTrue(isinstance(self.image_pic, Image))    

    def test_save_image(self):
        self.image_test.save_image()
        