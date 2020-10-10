from django.test import TestCase
from .models import Image

class TestImage(TestCase):
    def setUp(self):
        self.image_pic = Image(id=1, title='image', description='This is photo gallery test')

    def test_instance(self):
        self.assertTrue(isinstance(self.image_pic, Image))    

    def test_save_image(self):
        self.image_pic.save_image()
        img = Image.objects.all()
        self.assertTrue(len(img) > 0)
        
    def test_get_image_by_id(self):
        found_image = self.image_pic.get_image_by_id(self.image_pic.id)
        images = Image.objects.filter(id=self.image_pic.id)
        self.assertFalse(found_image, images)    

    def tearDown(self):
        Image.objects.all().delete()
