import graphene

from graphene_django import DjangoObjectType
from todo.models import Todo, Project
class TodoType(DjangoObjectType):
    class Meta:
        model = Todo
        fields = '__all__'
class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'

class Query(graphene.ObjectType):
    all_todos = graphene.List(TodoType) #allTodos
    all_project = graphene.List(ProjectType)

    def resolve_all_todos(root, info): #получать getattr
        return Todo.objects.all()

    def resolve_all_project(root, info): #получать getattr
        return Project.objects.all()

schema = graphene.Schema(query=Query)
