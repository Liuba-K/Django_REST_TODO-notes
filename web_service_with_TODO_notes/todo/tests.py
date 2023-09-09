from django.test import TestCase
from rest_framework import serializers
from .models import Project, Todo
#APITestCase
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__   '
class TodoSerializerBase(serializers.ModelSerializer):
    class Meta:

        model = Todo
        fields = '__all__'
class TodoSerializer(serializers.ModelSerializer):
    project = ProjectSerializer()
    class Meta:
        model = Todo
        fields = '__all__'
