"""Artsforum module for displaying arts -- to be used in future analysis"""
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
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

class TestViews(TestCase):
    """Class for testing the views section"""
    def setUp(self):
        """ Initilaizing """
        self.client = Client()
        self.user= User.objects.create_user(username='nci2024', password='peaceinworld')
        self.user_staff= User.objects.create_user(username='nci2025_staff', password='peaceinworld',is_staff=True)
        self.client.login(username='nci2024', password='peaceinworld')

        self.event = Community.objects.create(
            heading='test heading',
			location='Dublin',
			subline="Test Subline",
            seats=20,
			user_id=self.user_staff
		)

        self.community = reverse('index_comm')
        self.create_event = reverse('create_event')
        self.booking = reverse('booking',args=[self.event.id])
        self.view_part=reverse('view_part',args=[self.event.id])
        self.event_delete=reverse('event_delete',args=[self.event.id])


    def test_index(self):
        """Index event page"""
        response = self.client.get(self.community)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index_comm.html')

    def test_index_book_self(self):
        """test for booking the event"""
        response = self.client.post(self.community, {
			'book_me': True,
			'id': self.event.id
		})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Participants.objects.count(),1)

    def test_index_book_cancel(self):
        """test for cancelling the event"""
        response = self.client.post(self.community, {
			'id': self.event.id
		})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Participants.objects.count(),0)

    def test_booking(self):
        """Index booking page"""
        response = self.client.get(self.booking)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking.html')

    def test_create_event(self):
        """event creation page"""
        response = self.client.get(self.create_event)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_event.html')

    def test_create_event(self):
        """posting an event"""
        self.client.logout()
        self.client.login(username='nci2025_staff', password='peaceinworld')
        response=self.client.post(self.create_event,{
            'heading':'test heading',
			'location':'Dublin',
			'subline':"Test Subline",
            'seats':20,
			'user_id':self.user_staff
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Community.objects.count(),2)
        self.assertEqual(Community.objects.last().heading, 'test heading')

    def test_view_participants(self):
        """event creation page"""
        response = self.client.get(self.view_part)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'partdata.html')


