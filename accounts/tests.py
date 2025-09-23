from django.test import TestCase
from django.urls import reverse

from .models import CustomUser


class AccountTest(TestCase):
    username = 'user1'
    password = 'iuhfauiflkm34Ss'
    email = 'sfnnf@gmail.com'
    nat_id = '1452451285'

    @classmethod
    def setUpTestData(cls):
        CustomUser.objects.create_user(
            username=cls.username,
            password=cls.password,
            email=cls.email,
            nat_id=cls.nat_id,
        )

    def test_custom_user_creation(self):
        self.assertEqual(CustomUser.objects.all().count(), 1)
        self.assertEqual(CustomUser.objects.first().username, self.username)
        self.assertEqual(CustomUser.objects.last().email, self.email)
        self.assertEqual(CustomUser.objects.all()[0].nat_id, self.nat_id)

    def test_account_not_logged_in(self):
        response1 = self.client.get(reverse('signup'))
        self.assertEqual(response1.status_code, 200)
        self.assertTemplateUsed(response1, 'registration/signup.html')

        response2 = self.client.get('/accounts/signup/')
        self.assertEqual(response2.status_code, 200)
        self.assertContains(response2, 'form')

        response3 = self.client.get('/accounts/login/')
        self.assertEqual(response3.status_code, 200)
        self.assertTemplateUsed(response3, 'registration/login.html')

        response4 = self.client.get(reverse('login'))
        self.assertEqual(response4.status_code, 200)
        self.assertContains(response4, 'form')

    def test_signup(self):
        response = self.client.post(reverse('signup'), {
            'username': 'user2',
            'nat_id': '4715201236',
            'email': 'email@email.com',
            'password1': 'jaf87HGNbfal',
            'password2': 'jaf87HGNbfal',
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(CustomUser.objects.filter(email='email@email.com').exists())

    def test_log_in_log_out(self):
        response1 = self.client.post(reverse('login'), {
            'username': self.username,
            'password': self.password,
        })
        self.assertEqual(response1.status_code, 302)

        response2 = self.client.get(reverse('signup'))
        self.assertContains(response2, 'You have logged in!')

        response3 = self.client.get(reverse('login'))
        self.assertContains(response3, 'You have already logged in!')

        response4 = self.client.post(reverse('logout'))
        self.assertEqual(response4.status_code, 302)

    def test_change_password(self):
        response1 = self.client.post(reverse('login'), {
            'username': self.username,
            'password': self.password,
        })
        response2 = self.client.get(reverse('password_change'))
        self.assertTemplateUsed(response2, 'registration/password_change_form.html')

        response3 = self.client.post(reverse('password_change'), {
            "old_password": self.password,
            "new_password1": 'afj0f8dRafj8a0',
            "new_password2": 'afj0f8dRafj8a0',
        })
        self.assertEqual(response3.status_code, 302)

        response3 = self.client.get(reverse('password_change_done'))
        self.assertTemplateUsed(response3, 'registration/password_change_done.html')

    def test_reset_password(self):
        response1 = self.client.get(reverse('password_reset'))
        self.assertEqual(response1.status_code, 200)
        self.assertContains(response1, 'form')
        self.assertTemplateUsed(response1, 'registration/password_reset_form.html')

        response2 = self.client.post(reverse('password_reset'), {
            'email': self.email,
        })
        self.assertEqual(response2.status_code, 302)

        response3 = self.client.get(reverse('password_reset_done'))
        self.assertTemplateUsed(response3, 'registration/password_reset_done.html')
