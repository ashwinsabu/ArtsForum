"""Artsforum module for displaying arts -- to be used in future analysis"""
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Posts,UserRequest

# Create your tests here.
class TestModels(TestCase):
    """Class for testing the models section"""
    def setUp(self):
        """Function for initilaizing user to be used accross the class"""
        self.user= User.objects.create_user(username='nci2024', password='peaceinworld')

    def test_model_posts(self):
        """Function for creating model for post module"""
        post_item = Posts.objects.create(
            image='./image/test_image.jpg',
			name='Test Post',
			description="Test Description",
			user_created=self.user
		)
        self.assertEqual(str(post_item), 'Test Post')
        self.assertTrue(isinstance(post_item, Posts))

    def test_model_contacts(self):
        """Function for creating model for contact us queries"""
        post_contact = UserRequest.objects.create(
			name='Test Contact',
            email='ashwin@a.com',
			message="Test message",
			vol_assign=self.user,
            status=0,
            comments='Test Comments'
		)
        self.assertEqual(str(post_contact), 'Test Contact')
        self.assertTrue(isinstance(post_contact, UserRequest))
