from django.test import TestCase
from .models import Profile,Projects
from django.contrib.auth.models import User
# Create your tests here.

class ProfileTest(TestCase):
    def setUp(self):
        self.jeff = User(username = 'Jeff',email = 'jeffmwai3@gmail.com')
        self.jeff = Profile(user = Self.jeff,user = 1,Bio = 'tests',photo = 'test.jpg',date_created='Nov,30.2020')

    def test_instance(self):
        self.assertTrue(isinstance(self.jeff,Profile))

    def test_save_profile(self):
        Profile.save_profile(self)
        all_profiles = Profile.objects.all()
        self.assertTrue(len(all_profiles),0)

    def test_delete_profile(self):
        self.jeff.delete_profile()
        all_profiles = Profile.objects.all()
        self.assertEqual(len(all_profiles),0)