#from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer, StringRelatedField
from .models import Project, Todo


class ProjectModelSerializer(ModelSerializer):
    users = StringRelatedField(many=True) #user будет представлен методом __str__ в модели Author,
    # а ключ many=True позволяет выводить несколько пользователей.

    class Meta:
        model = Project
        fields = '__all__'


class TodoModelSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
