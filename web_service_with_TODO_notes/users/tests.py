import json # для чтения содержимого ответа от сервера;
from django.test import TestCase #базовый класс для создания Django-теста;
from rest_framework import status #status это константы коды для всех ответов http
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase,APITestCase
"""
APIRequestFactory — фабрика для создания запросов;
force_authenticate — функция для авторизации пользователя;
APIClient — клиент для удобной отправки REST-запросов;
APISimpleTestCase — класс для создания простых test cases;
APIITestCase — класс для создания test cases для REST API;
"""
from django.contrib.auth.models import User
from .views import UserAPIView, UserModelSerializer, UserListAPIView
from .models import User
from mixer.backend.django import mixer #библиотека для генерации тестовых данных;

class TestUserView(TestCase):

    def test_get_list(self): #проверять страницу со списком пользователей
        factory = APIRequestFactory()
        request = factory.get('/api/users/')

        view = UserListAPIView.as_view({'get': 'list'}) #если mixin
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_guest(self): # запрос на создание пользователя, который отправляет неавторизованный пользователь.
        factory = APIRequestFactory()

        request = factory.post('/api/users/', {'username': 'Liuba1', 'firstname': 'Люба1', 'lastname': 'Кундас1', 'email': 'kundasl11@gmail.com'}, format='json')
        view = UserListAPIView.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
# python manage.py test

    def test_create_admin(self):
        factory = APIRequestFactory()

        request = factory.post('/api/users/', {'username': 'Liuba', 'firstname': 'Люба', 'lastname': 'Кундас', 'email': 'kundasl1@gmail.com'}, format='json')
        #admin = User.objects.create_superuser('admin', 'admin@admin.com',
                                              'Rustle14')
        force_authenticate(request, admin)
        view = UserListAPIView.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#APIClient()
def test_get_detail(self):
    author = User.objects.create(username='Liuba', firstname='Люба', lastname='Кундас', email='kundasl1@gmail.com')

    client = APIClient()
    #response = client.get(f'/api/users/{user.id}/')
    self.assertEqual(response.status_code, status.HTTP_200_OK)

#APISimpleTestCase
class TestMath(APISimpleTestCase):
    def test_sqrt(self):
        import math
        self.assertEqual(math.sqrt(4), 2)


