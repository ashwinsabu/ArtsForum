"""Artsforum module for displaying arts -- to be used in future analysis"""
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Community, Participants

# Create your tests here.
class TestModels(TestCase):
    """Class for testing the models section"""
    def setUp(self):
        """Function for initilaizing user to be used accross the class"""
        self.user= User.objects.create_user(username='nci2024', password='peaceinworld')
        self.community= Community.objects.create(heading='test', location='test',subline='test',seats=20)

    def test_model_community(self):
        """Function for creating model for event module"""
        event_item = Community.objects.create(
            heading='test heading',
			location='Dublin',
			subline="Test Subline",
            seats=20,
			user_id=self.user
		)
        self.assertEqual(str(event_item), 'test heading')
        self.assertTrue(isinstance(event_item, Community))

    def test_model_participants(self):
        """Function to records participants"""
        part_creation = Participants.objects.create(
			name='Ashwin',
            email='ashwin@a.com',
            age=20,
            number=26478298412,
			user_id=self.user,
            community_id=self.community,
		)
        self.assertEqual(str(part_creation), self.user.username)
        self.assertTrue(isinstance(part_creation, Participants))
