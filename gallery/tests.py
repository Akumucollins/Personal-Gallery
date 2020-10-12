from django.test import TestCase
from .models import Image,Location,Category

class TestImage(TestCase):
    def setUp(self):
        self.image_pic = Image(id=1, title='image', description='This is photo gallery test')

        self.location = Location(name='Nairobi')
        self.location.save_location()

        self.category = Category(name='drinks')
        self.category.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.image_pic, Image))    

    def test_save_image(self):
        self.image_pic.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_image(self):
        self.image_pic.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)    
        
    def test_get_image_by_id(self):
        found_image = self.image_pic.get_image_by_id(self.image_pic.id)
        images = Image.objects.filter(id=self.image_pic.id)
        self.assertFalse(found_image, images)    

    def test_update_image(self):
        self.image_pic.save_image()
        self.image_pic.update_image(self.image_pic.id, 'images/photo1.jpg')
        updated_image = Image.objects.filter(image='images/photo2.jpg')
        self.assertFalse(len(updated_image) > 0)

    def test_search_by_location(self):
        self.image_test.save_image()
        found_images = self.image_test.filter_by_location(location='moringa')
        self.assertTrue(len(found_images) == 1)

    def test_search_by_category(self):
        category = 'technology'
        found_img = self.image_test.search_by_category(category)
        self.assertTrue(len(found_img) > 1)    

    def test_view_location(self):
        self.image_pic.save()
        location = Image.view_location(self.location)
        self.assertTrue(len(location) > 0)

    def test_view_category(self):
        self.image_pic.save()
        categories = Image.view_category(self.category)
        self.assertTrue(len(categories) > 0)  

    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()

class TestLocation(TestCase):
    def setUp(self):
        self.location = Location(name='Nairobi')
        self.location.save_location()

    def test_instance(self):
        self.location.save()
        self.assertTrue(isinstance(self.location, Location))

    def test_save_location(self):
        self.location.save_location()
        location_test = Location.get_location()
        self.assertTrue(len(location_test) > 0)

    def test_get_location(self):
        self.location.save_location()
        location_test = Location.get_location()
        self.assertFalse(len(location_test) > 1)

    def test_upt_location(self):
        new_location = 'Delhi'
        self.location.upt_location(self.location.id, new_location)
        location_uptd = Location.objects.filter(name='Dar es Salaam')
        self.assertTrue(len(location_uptd) > 0)

    def test_del_location(self):
        self.location.del_location()
        location_test = Location.objects.all()
        self.assertTrue(len(location_test) == 0)    

class CategoryTestClass(TestCase):
    def setUp(self):
        self.category = Category(name='food')
        self.category.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_category(self):
        self.category.save_category()
        cat = Category.objects.all()
        self.assertTrue(len(cat) > 0)        