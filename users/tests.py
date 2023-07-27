from django.contrib.auth.models import User
from django.test import TestCase
from http import HTTPStatus
from django.urls import reverse
from learning_logs.models import Section, Model


class UserRegistrationViewTestCase(TestCase):
    """Tests for REGISTRATION"""

    def setUp(self):
        """General variables with help setUp"""
        self.path = reverse('users:register')
        self.data = {
            'username': 'ninjame',
            'password1': 'Middleweightchampion1',
            'password2': 'Middleweightchampion1'
        }

    def test_user_register_success_get(self):
        """Check on status_code and used templates"""
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'registration/register.html')

    def test_user_register_success_post(self):
        """
        Test for absence of a user, success register and if success, we redirects to
        index.html and check and the fact that he is present with success
        """
        username = self.data['username']
        self.assertFalse(User.objects.filter(username=username).exists())

        response = self.client.post(self.path, self.data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse('learning_logs:index'))
        self.assertTrue(User.objects.filter(username=username).exists())

    def test_user_register_error_post(self):
        """Check for busy username"""
        User.objects.create(username=self.data['username'])
        response = self.client.post(self.path, self.data)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, 'A user with that username already exists.', html=True)


class UserLoginTestCase(TestCase):
    """Tests for LOGIN"""

    def setUp(self):
        """General variables with help setUp"""
        self.path = reverse('users:login')
        self.data = {
            'username': 'ninjame',
            'password': 'Middleweightchampion1'
        }

    def test_user_login_success_post(self):
        """
        Tests for LOGIN PAGE, check status_code, check used templates
        success redirect message
        """
        response = self.client.post(self.path, self.data)
        self.assertEquals(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'registration/login.html')
        self.assertContains(response, '', html=True)

    def test_user_login_error_post(self):
        """
        Tests for LOGIN PAGE, check status_code, check used templates
        success redirect message
        """
        response = self.client.post(self.path, self.data)
        self.assertEquals(response.status_code, HTTPStatus.OK)
        self.assertContains(response, '', html=True)


class UserLogoutTestCase(TestCase):
    """Tests for LOGOUT"""
    def setUp(self):
        """General variables with help setUp"""
        self.path = reverse('users:logged_out')
        self.response = self.client.post(self.path)

    def test_user_logout_success_get(self):
        """If we successfully logout we redirects to logout page(main page),check status code
         and if we go out we get a message"""
        self.assertEqual(self.response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(self.response, 'registration/logged_out.html')
        self.assertContains(self.response, 'You have been logget out. Thank you for visiting!', html=True)

