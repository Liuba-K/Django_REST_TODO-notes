from rest_framework.viewsets import ModelViewSet  #нужно??

from .models import Project, Todo
from .serializers import ProjectModelSerializer, TodoModelSerializer


class TodoModelViewSet(ModelViewSet):
    queryset = Todo.objects.all() #почему  objects загорелся?
    serializer_class = TodoModelSerializer


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all() #точно all?
    serializer_class = ProjectModelSerializer


