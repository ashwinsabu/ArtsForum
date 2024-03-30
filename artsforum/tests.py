"""Artsforum module for displaying arts -- to be used in future analysis"""
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
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

class TestViews(TestCase):
    """Class for testing the views section"""
    def setUp(self):
        """ Initilaizing """
        self.client = Client()
        self.user= User.objects.create_user(username='nci2024', password='peaceinworld',is_staff=True)
        self.client.login(username='nci2024', password='peaceinworld')

        self.post_new = Posts.objects.create(
            image='./image/test_image.jpg',
			name='Test Post',
			description="Test Description",
			user_created=self.user
		)


        self.request_new= UserRequest.objects.create(
			name='Test Contact',
            email='ashwin@a.com',
			message="Test message 101",
			vol_assign=self.user,
            status=0,
            comments='Test Comments'
		)

        #urls section
        self.about = reverse('about')
        self.index = reverse('index')
        self.contact = reverse('contact')
        self.post = reverse('post')
        self.query=reverse('query')
        self.logout=reverse('logout')

    def test_about(self):
        """About us page"""
        response = self.client.get(self.about)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/about.html')

    def test_index(self):
        """Index page"""
        response = self.client.get(self.index)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/index.html')
    
    def test_delete_post(self):
        """test for deleting the post"""
        response = self.client.post(self.index, {
			'delete_admin': True,
			'post_id': self.post_new.id
		})
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Posts.objects.filter(id=self.post_new.id).exists())

    def test_contact(self):
        """contact page"""
        response = self.client.get(self.contact)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/contact.html')

    def test_contact_post(self):
        """posting a query"""
        response=self.client.post(self.contact,{
            'name':"Ashwin",
            'email':"ashwin@ashwin.com",
            'message':"Test message",
            'comments':"Test comments",
            'vol_assign':self.user,
            'status':0
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(UserRequest.objects.count(), 2)
        self.assertEqual(UserRequest.objects.last().name, 'Ashwin')

    def test_post(self):
        """post page"""
        response = self.client.get(self.post)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/create_post.html')

    def test_content_post(self):
        """posting a content"""
        response=self.client.post(self.post,{
            'image':'./image/test_image.jpg',
			'name':'Test Post',
			'description':"Test Description",
			'user_created':self.user
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Posts.objects.count(), 1)
        self.assertEqual(Posts.objects.last().name, 'Test Post')

    def test_query(self):
        """query page"""
        response = self.client.get(self.query)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/query.html')

    def test_query_update(self):
        """test for deleting the post"""
        response = self.client.post(self.query, {
			'change': True,
            'comments':"Test comments 2024",
			'id': self.request_new.id
		})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(UserRequest.objects.get(id=self.request_new.id).comments,'Test comments 2024')

    def logout(self):
        """logout"""
        response = self.client.get(self.logout)
        self.assertEqual(response.status_code, 302)