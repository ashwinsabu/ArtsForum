"""Bids module for displaying arts"""
from django.test import TestCase, Client
from django.contrib.auth.models import User
from datetime import datetime
from django.urls import reverse
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

class TestViews(TestCase):
    """Class for testing the views section"""
    def setUp(self):
        """ Initilaizing """
        self.client = Client()
        self.user_1= User.objects.create_user(username='nci2024', password='peaceinworld',is_staff=True)
        self.user_2= User.objects.create_user(username='nci_2025', password='peaceinworld',is_staff=False)
        self.client.login(username='nci2024', password='peaceinworld')

        self.bidpost=BidPosts.objects.create(
            image='./image/test_image.jpg',
			name='Test Bid',
			description="Test Description",
			user_created=self.user_1,
            user_assigned=self.user_2,
            amount_initial=10,
            amount_final=200,
            time_limit=datetime(2025,11,1,10,0,0),
            Status=0
		)

        self.bid_index = reverse('bid_index')
        self.create_bid = reverse('create_bid')
        self.myposts = reverse('myposts')

    def test_index_bid(self):
        """Index page"""
        response = self.client.get(self.bid_index)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bid_index.html')

    def test_play_bid(self):
        """Allow other users to bid on active bids"""
        response = self.client.post(self.bid_index, {
			'bid': True,
            'post_id':self.bidpost.id,
            'amount_final':200,
			'user_id': self.user_2.id
		})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(BidPosts.objects.get(id=self.bidpost.id).user_assigned_id,self.user_2.id)

    def test_delete_bid(self):
        """Allow supervisors to delete bids"""
        response = self.client.post(self.bid_index, {
			'delete_admin': True,
            'post_id':self.bidpost.id,
		})
        self.assertEqual(response.status_code, 302)
        self.assertFalse(BidPosts.objects.filter(id=self.bidpost.id).exists())

    def test_view_create_bid(self):
        """Create Bid View page"""
        response = self.client.get(self.create_bid)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create.html')
    
    def test_my_posts(self):
        """Create Bid page"""
        response = self.client.get(self.myposts)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mybid.html')



