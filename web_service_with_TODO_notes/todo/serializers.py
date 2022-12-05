#from rest_framework.relations import StringRelatedField
from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Project, Todo
#from ..users.serializers import UserModelSerializer


class ProjectModelSerializer(HyperlinkedModelSerializer):
    #users = StringRelatedField(many=True) #user будет представлен методом __str__ в модели Author,
    # а ключ many=True позволяет выводить несколько пользователей.

    class Meta:
        model = Project
        fields = '__all__'


class TodoModelSerializer(HyperlinkedModelSerializer):
    #user = UserModelSerializer(many=True)
    #users = StringRelatedField(many=True)

    class Meta:
        model = Todo
        fields = '__all__'
