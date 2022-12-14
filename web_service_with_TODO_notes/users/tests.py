import json
from django.test import TestCase
from rest_framework import status
#status это константы коды для всех ответов http
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase,APITestCase
from django.contrib.auth.models import User
from .views import UserAPIView, UserModelSerializer,UserListAPIView
from .models import User


class TestUserView(TestCase):

    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/users/')
        view = UserListAPIView.as_view({'get': 'list'}) #если mixin
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
