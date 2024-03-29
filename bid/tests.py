"""Bids module for displaying arts"""
from django.test import TestCase
from django.contrib.auth.models import User
from datetime import datetime
from .models import BidPosts

# Create your tests here.
class TestModels(TestCase):
    """Class for testing the models section"""
    def setUp(self):
        """Function for initilaizing user to be used accross the class"""
        self.user1= User.objects.create_user(username='nci2024', password='peaceinworld')
        self.user2= User.objects.create_user(username='staff_2024', password='peaceinworld')

    def test_model_bids(self):
        """Function for creating bids contents"""
        bid_item = BidPosts.objects.create(
            image='./image/test_image.jpg',
			name='Test Bid',
			description="Test Description",
			user_created=self.user1,
            user_assigned=self.user2,
            amount_initial=10,
            amount_final=200,
            time_limit=datetime(2025,11,1,10,0,0),
            Status=0
		)
        self.assertEqual(str(bid_item), 'Test Bid')
        self.assertTrue(isinstance(bid_item, BidPosts))


