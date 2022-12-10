from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string


class Command(BaseCommand):
    help = u'Создание случайного пользователя'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help=u'Количество создаваемых пользователей')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        for i in range(total):
            User.objects.create_user(username=get_random_string(), email='', password='123')

#python manage.py create_auto_user 10 указать сколько создать тестовых пользователей