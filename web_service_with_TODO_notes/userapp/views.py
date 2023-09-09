from rest_framework.generics import ListAPIView
from django.contrib.auth.models import User
from userapp.serializers import UserModelSerializer, UserFullModelSerializer
class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    def get_serializer_class(self):
        if self.request.version == 'v2':
            return UserFullModelSerializer
        return UserModelSerializer