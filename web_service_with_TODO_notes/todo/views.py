#from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet

from .models import Project, Todo
from .serializers import ProjectModelSerializer, TodoModelSerializer


from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer

from rest_framework.response import Response
"""
class TodoModelViewSet(ModelViewSet):
    queryset = Todo.objects.all() #почему  objects загорелся?
    serializer_class = TodoModelSerializer


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all() #точно all?
    serializer_class = ProjectModelSerializer
"""


class ProjectAPIView(APIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer

#paginator
class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


#filter
class ProjectModelViewSetFilter(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = ProjectLimitOffsetPagination

    def get_queryset(self):
        name = self.request.query_params('name', '')
        project = Project.objects.all()
        if name:
            project = project.filter(name__contains=name)
        return project

class TodoAPIView(APIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    #queryset = Todo.objects.all()
    #serializer_class = TodoModelSerializer

    def get(self, request, format=None):
        queryset = Todo.objects.all()
        serializer = TodoModelSerializer(queryset, many=True)
        return Response(serializer.data)

    def delete(self, request, format=None):
        return "closed"
    # при удалении не удалять ToDo, а выставлять признак, что оно закрыто;

#paginator
class TodotLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20

#filter
class TodoModelViewSetFilter(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer
    pagination_class = TodotLimitOffsetPagination
    filterset_fields = ['created']
#Передадим 2 даты, дату начала и окончания (ссылка).


