from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class TestAuthViews(TestCase):
    """
    This class contains tests for the authentication views.
    """

    def setUp(self):
        self.login_url = reverse('login')
        self.signup_url = reverse('signup')
        self.logout_url = reverse('logout')
        self.reset_password_url = reverse('password_reset')
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.home_url = reverse('home')

    def test_login_view(self):
        """
        Test that the login view returns a status code of 200 and uses the correct template.
        """
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_signup_view(self):
        """
        Test that the signup view returns a status code of 200 and uses the correct template.
        """
        response = self.client.get(self.signup_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')

    def test_logout_view(self):
        """
        Test that the logout view redirects to the home page after logging out.
        """
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.logout_url)
        self.assertRedirects(response, self.home_url)

    def test_password_reset_view(self):
        """
        Test that the password reset view returns a status code of 200 and uses the correct template.
        """
        response = self.client.get(self.reset_password_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/password_reset_form.html')

    def test_login_functionality(self):
        """
        Test that a user can successfully log in with valid credentials and is redirected to the home page.
        """
        login_data = {'username': 'testuser', 'password': 'testpass'}
        response = self.client.post(self.login_url, login_data)
        self.assertRedirects(response, self.home_url)

    def test_signup_functionality(self):
        """
        Test that a user can successfully sign up with valid credentials and is redirected to the login page.
        """
        signup_data = {'username': 'newuser', 'password1': 'newpass123', 'password2': 'newpass123'}
        response = self.client.post(self.signup_url, signup_data)
        self.assertRedirects(response, self.login_url)


class TemplateTests(TestCase):
    """
     Test login template
     """
    def test_login_template(self):
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'registration/login.html')
        self.assertContains(response, 'Login')
        self.assertContains(response, 'Username')
        self.assertContains(response, 'Password')

    """
     Test signup template
     """
    def test_signup_template(self):
        response = self.client.get(reverse('signup'))
        self.assertTemplateUsed(response, 'registration/signup.html')
        self.assertContains(response, 'Sign up')
        self.assertContains(response, 'Username')
        self.assertContains(response, 'Password')
        self.assertContains(response, 'Password confirmation')

    """
    Test password reset template
    """
    def test_password_reset_template(self):
        response = self.client.get(reverse('password_reset'))
        self.assertTemplateUsed(response, 'registration/password_reset_form.html')
        self.assertContains(response, 'Email')

    """
    Test password reset done template
    """
    def test_password_reset_done_template(self):
        response = self.client.get(reverse('password_reset_done'))
        self.assertTemplateUsed(response, 'registration/password_reset_done.html')
        self.assertContains(response, "We've emailed you instructions for setting your password. "
                                      "You should receive the email shortly!")
