#from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import UserModelSerializer
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer

from rest_framework.response import Response

"""
class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all() #точно all?
    serializer_class = UserModelSerializer
"""
#есть возможность просмотра списка и каждого пользователя в отдельности, можно вносить изменения, нельзя удалять и создавать;
class UserAPIView(APIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    #queryset = User.objects.all()
    #serializer_class = UserModelSerializer

    def get(self, request, format=None):
        users = User.objects.all()

        serializer = UserModelSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        pass

