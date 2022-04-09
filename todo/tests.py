from django.test import TestCase
import json
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from django.contrib.auth.models import User
from .models import TodoModel, ProjectModel
from authors.models import Author
from authors.views import AuthorModelViewSet
from .views import ProjectView, TodoView


# APIRequestFactory «подменяет» объект запроса, который мы потом передаём во view.
#                       Этот класс:
#                         ● возвращает объект запроса;
#                         ● не делает настоящий запрос;
#                         ● используется для изолированной проверки view;
#                         ● используется редко, обычно для нестандартных случаев.
# APIClient — класс для удобной отправки REST-запросов  и сразу получать ответ. Этот класс используется наиболее часто.
#                       Этот класс:
#                         ● отправляет запрос;
#                         ● обычно используется для большинства тестов.
# APISimpleTestCase применяется очень редко: в случаях, когда тест не связан с базой данных.
#                       Этоткласс:
#                         ● не использует базу данных;
#                         ● удобен для тестирования внутренних функций;
#                         ● быстро исполняется.
#                         ● APITestCase.
#


# ● модуль json нужен для чтения содержимого ответа от сервера;
# ● TestCase — базовый класс для создания Django-теста;
# ● status содержит константы для ответов сервера;
# ● APIRequestFactory — фабрика для создания запросов;
# ● force_authenticate — функция для авторизации пользователя;
# ● APIClient — клиент для удобной отправки REST-запросов;
# ● APISimpleTestCase — класс для создания простых test cases;
# ● APIITestCase — класс для создания test cases для REST API;
# ● Mixer — библиотека для генерации тестовых данных;
# ● User — модель пользователя;
# ● AuthorModelViewSet — view set для работы с моделью Author;
# ● TodoModel, ProjectModel, Author — модели.

user_model = Author.objects.first()
project_model = ProjectModel.objects.first()


class TestAuthorViewSet(TestCase):

    # APIRequestFactory
    def test_get_list_author(self):
        factory = APIRequestFactory()
        request = factory.get('api/authors/')
        view = AuthorModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_list_project(self):
        factory = APIRequestFactory()
        request = factory.get('api/projects/')
        view = ProjectView.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_list_project_authenticate_user(self):
        factory = APIRequestFactory()
        request = factory.get('api/projects/')
        admin = User.objects.create_superuser('admin', 'admin@com.com', 'admin123456')
        force_authenticate(request, admin)
        view = ProjectView.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_author(self):
        factory = APIRequestFactory()
        request = factory.post('api/authors/', {'first_name': 'Djon',
                                                'last_name': 'Puchin',
                                                'birthday_year': '1991',
                                                'email': 'puchin@mail.ru',
                                                'position': 'developer'})
        view = AuthorModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_project(self):
        factory = APIRequestFactory()
        request = factory.post('api/project/', {'project_name': 'сайт для ВАС',
                                                'users': user_model,
                                                'link_git': 'git/mru.com',
                                                'descriptions': '........'})
        view = ProjectView.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_todo(self):
        factory = APIRequestFactory()
        request = factory.post('api/project/', {'project': project_model,
                                                'todo_descriptions': 'сделать верстку и макет',
                                                'users': user_model})
        view = TodoView.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_admin(self):
        factory = APIRequestFactory()
        request = factory.post('api/author/', {'first_name': 'Djon',
                                                'last_name': 'Puchin',
                                                'birthday_year': '1991',
                                                'email': 'puchin@mail.ru',
                                                'position': 'developer'})
        admin = User.objects.create_superuser('admin', 'admin@com.com', 'admin123456')
        force_authenticate(request, admin)
        view = AuthorModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # APIClient
    def test_get_detail(self):
        author = Author.objects.create(first_name='Djon',
                                       last_name='Puchin',
                                       birthday_year='1991',
                                       email='puchjjin@mail.ru',
                                       position='developer')
        client = APIClient()
        response = client.get(f'/api/author/{author.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_author(self):
        author = Author.objects.create(first_name='Djon',
                                       last_name='Puchin',
                                       birthday_year='1991',
                                       email='puin@mail.ru',
                                       position='developer')
        client = APIClient()
        response = client.put(f'/api/author/{author.id}/', {'first_name': 'jek',
                                                            'last_name': 'Pushilin',
                                                            'birthday_year': '1991',
                                                            'email': 'jek@mail.ru',
                                                            'position': 'developer'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_edit_author_and_authorize(self):
        author = Author.objects.create(first_name='Djon',
                                       last_name='Puchin',
                                       birthday_year='1991',
                                       email='puin@mail.ru',
                                       position='developer')
        client = APIClient()
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        client.login(username=admin, password='admin123456')
        response = client.put(f'/api/author/{author.id}/', {'first_name': 'jek',
                                                            'last_name': 'Pushilin',
                                                            'birthday_year': '1991',
                                                            'email': 'jek@mail.ru',
                                                            'position': 'developer'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        author = Author.objects.get(id=author.id)
        self.assertEqual(author.first_name, 'jek')
        self.assertEqual(author.email, 'jek@mail.ru')
        client.logout()

    # APISimpleTestCase

    def test_sqrt(self):
        import math
        self.assertEqual(math.sqrt(4), 2)

    # APITestCase
    def test_edit_project_for_admin(self):
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        self.client.login(username='admin', password='admin123456')
        response = self.client.get(f'/api/projects/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_project_for_admin(self):

        """TypeError: Direct assignment to the forward side of a many-to-many set is prohibited. Use users.set() instead."""

        user = Author.objects.create(first_name='Djon',
                                     last_name='Puchin',
                                     birthday_year='1991',
                                     email='puin@mail.ru',
                                     position='developer')
        project = ProjectModel.objects.create(project_name='сайт для ВАС',
                                              users=user,
                                              link_git='git/mru.com',
                                              descriptions='........')

        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        self.client.login(username='admin', password='admin123456')

        response = self.client.put(f'/api/projects/{project.id}/', {
            'project_name': 'сайт YouTube',
            'link_git': 'git/YouTube.com',
            'descriptions': 'YouTube Api user',
            'users': project.users.id
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_project_for_admin_mixer(self):

        """AttributeError: 'ManyRelatedManager' object has no attribute 'id'"""

        project = mixer.blend(ProjectModel)
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        self.client.login(username='admin', password='admin123456')
        print('---------8888888--------', project.users.id)
        response = self.client.put(f'/api/projects/{project.id}/', {
            'project_name': 'сайт YouTube',
            'link_git': 'git/YouTube.com',
            'descriptions': 'YouTube Api user',
            'users': project.users.id
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
