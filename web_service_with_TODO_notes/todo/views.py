#from rest_framework.generics import ListAPIView
from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.request import Request
from rest_framework.viewsets import ModelViewSet

from users.serializers import UserModelSerializer
from .models import Project, Todo
from .serializers import ProjectModelSerializer, TodoModelSerializer


from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
"""
class TodoModelViewSet(ModelViewSet):
    queryset = Todo.objects.all() #почему  objects загорелся?
    serializer_class = TodoModelSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    

class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all() #точно all?
    serializer_class = ProjectModelSerializer
"""


class ProjectAPIView(APIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    #queryset = Project.objects.all()
    #serializer_class = ProjectModelSerializer

    def get(self, request: Request, id, format=None)-> Response:
        project = Project.objects.get(id=id)

        # id = request.query_params.get('id')
        # project = Project.objects.all()
        # if id:
            #project = Project.filter(id=id)

        serializer = ProjectModelSerializer(project)  # ,many=True
        return Response(serializer.data)



class ProjectListAPIView(APIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get(self, request: Request, format=None)-> Response:
        #user_detail = UserViewSet.as_view({'get': 'retrieve'})
        projects = Project.objects.all()
        serializer = ProjectModelSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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

#new filter django
class ProjectDjangoFilterViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    filterset_fields = ['name_project', 'users']
    #filterset_class = ProjecrFilter


class TodoAPIView(APIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    #queryset = Todo.objects.all()
    #serializer_class = TodoModelSerializer

    def get(self, request, format=None):
        queryset = Todo.objects.all()
        id = request.query_params.get('id')

        if id:
            queryset = Todo.filter(id=id)


        serializer = TodoModelSerializer(queryset, many=True)
        return Response(serializer.data)

    def delete(self, request, format=None):
        return "closed"
    # при удалении не удалять ToDo, а выставлять признак, что оно закрыто;

class TodoListAPIView(APIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get(self, request: Request, format=None)-> Response:
        todos = Todo.objects.all()
        serializer = TodoModelSerializer(todos, many=True)
        return Response(serializer.data)

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


