import graphene

from graphene_django import DjangoObjectType
from todo.models import Todo, Project
from users.models import User

class TodoType(DjangoObjectType):
    class Meta:
        model = Todo
        fields = '__all__'
class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'

class Query(graphene.ObjectType):

    all_todos = graphene.List(TodoType) #allTodos
    all_project = graphene.List(ProjectType)
    project_by_id = graphene.Field(ProjectType, id=graphene.Int(required=True))
    #фильтрация пример
    todos_by_project_name = graphene.List(TodoType, name=graphene.String(required=True))

    all_users = graphene.List(UserType)

    def resolve_all_todos(root, info): #получать getattr
        return Todo.objects.all()

    def resolve_todos_by_project_name(root, info, name):
        todos = Todo.objects.all()
        #projects = Project.objects.all()
        if name:
            todos = todos.filter(project__name=name)
        return todos


    def resolve_all_project(root, info): #получать getattr
        return Project.objects.all()

    def resolve_project_by_id(root, self, id):
        try:
            return Project.objects.get(pk=id)
        except Project.DoesNotExist:
            return None

    def resolve_all_users(root, info): #allUsers
        return User.objects.all()

class TodoMutation(graphene.Mutation):
    class Arguments:
        text = graphene.Int(required=True)
        user = graphene.ID()
    todo = graphene.Field(TodoType)

    @classmethod
    def mutate(cls, root, text, user):
        todo = Todo.objects.get(pk=id)
        todo.text = text
        todo.save()
        return TodoMutation(todo=todo)

class Mutation(graphene.ObjectType):
    update_todo = TodoMutation.Field()



schema = graphene.Schema(query=Query, mutation=Mutation)
