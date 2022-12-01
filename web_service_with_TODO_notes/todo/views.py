#from rest_framework.viewsets import ModelViewSet

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


