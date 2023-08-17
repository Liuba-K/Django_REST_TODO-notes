from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


class UserFullModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'is_superuser', 'is_staff')
