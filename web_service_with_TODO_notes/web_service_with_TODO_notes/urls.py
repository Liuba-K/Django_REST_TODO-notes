"""web_service_with_TODO_notes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from graphene_django.views import GraphQLView
from rest_framework import permissions
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

#from users.views import UserModelViewSet
#from todo.views import TodoModelViewSet, ProjectModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from todo.views import TodoAPIView, ProjectAPIView, ProjectModelViewSetFilter, TodoModelViewSetFilter, \
    ProjectListAPIView, TodoListAPIView, ProjectDjangoFilterViewSet
from users.views import UserAPIView, UserListAPIView
from userapp.views import UserListAPIView

schema_view = get_schema_view(
    openapi.Info(
        title='Todo',
        default_version='v1',
        description='Documentation to out project',
        contact=openapi.Contact(email='admin@admin.local'),
        license=openapi.License(name='MIT License'),

    ),
    public=True,
    permission_classes=[permissions.AllowAny], #права на документацию.IsAuthenticated

)

router = DefaultRouter()
#router.register('users', UserModelViewSet)
#router.register('todo', TodoModelViewSet)
#router.register('project', ProjectModelViewSet)
router.register('project_filter', ProjectModelViewSetFilter)
router.register('project_filter', ProjectDjangoFilterViewSet)
router.register('project_filter', TodoModelViewSetFilter)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', views.obtain_auth_token),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/user/<int:id>/', UserAPIView.as_view()), #конкретная переменная
    path('api/users/', UserListAPIView.as_view()),
    path('api/todos/', TodoListAPIView.as_view()),
    path('api/todo/<int:id>/', TodoAPIView.as_view()),
    path('api/projects/', ProjectListAPIView.as_view()),
    path('api/project/<int:id>/', ProjectAPIView.as_view()),

    path('api/<str:version>/users/', UserListAPIView.as_view()),
    #path('swagger<str:format>/', schema_view.without_ui()),#просто вызвать серилизацию
    path('swagger/', schema_view.with_ui('swagger')),
    path('redoc/', schema_view.with_ui('redoc')),
    path('graphql/', GraphQLView.as_view(graphiql=True)),


]
