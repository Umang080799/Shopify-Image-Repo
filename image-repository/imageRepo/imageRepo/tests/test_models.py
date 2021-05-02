from django.test import TestCase
from ..models import imageRepo

# Function to test the data field image titile
# of the class ImageRepo 
class Tests(TestCase):

    # Runs once before every test case
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        imageRepo.objects.create(title='Test1')

    # Checks if the value of title is Test1
    def test_classFields(self):
        entry = imageRepo.objects.get(pk=1)
        title = entry._meta.get_field('title')
        # Gets the value in the field title
        value = getattr(entry, title.attname)
        self.assertEqual(value,"Test1")
    
    # Asserts the max length of the title field to be 100
    def test_maxLenght(self):
        entry = imageRepo.objects.get(pk=1)
        max_length = entry._meta.get_field('title').max_length
        self.assertEqual(max_length,100)



    
