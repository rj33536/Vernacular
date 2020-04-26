from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

# Include an appropriate `Authorization:` header on all requests.
#token = Token.objects.get(user__username='lauren')
#client = APIClient()
#client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)


class LoginTests(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')

    def test_login_account(self):
        """
        Ensure we can create a new account object.
        """
        headers = {
            'Content-Type': 'application/json'
        }
        url = reverse('login')
        data = {'username': 'john','password':"johnpassword"}
        response = self.client.post(url, data,headers=headers, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(list(response.data.keys()),["user","token"])


'''
class HomeTests(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com', 'johnpassword')
              
        headers = {
            'Content-Type': 'application/json'
        }
        url = reverse('login')
        data = {'username': 'john','password':"johnpassword"}
        response = self.client.post(url, data,headers=headers, format='json')
        
        self.token = response.data['token'] 

    def test_home(self):
        """
        Ensure we can create a new account object.
        """
        headers = {
            'Content-Type': 'application/json',
            'Authorization':"Token  "+self.token
        }
        url = reverse('home')
        response = self.client.get(url,data={},headers=headers)
        print(response.data,headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(list(response.data.keys()),["id","username","email"])
'''