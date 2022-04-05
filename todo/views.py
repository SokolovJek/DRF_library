from .models import ProjectModel, TodoModel
from .serializers import ProjectModelSerializers, TodoModelSerializers
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import UpdateModelMixin, RetrieveModelMixin, ListModelMixin, DestroyModelMixin, CreateModelMixin
from rest_framework.pagination import LimitOffsetPagination
from .filter import ProjectFilter, TodoFilter
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import BasePermission
from rest_framework.permissions import IsAuthenticated, AllowAny


class MyPaginator(LimitOffsetPagination):
    default_limit = 6


class MyPaginatorTodoView(LimitOffsetPagination):
    default_limit = 20


class StaffOnly(BasePermission):
    """Здесь правами будут наделены пользователи-сотрудники (is_staff)."""
    def has_permission(self, request, view):
        return request.user.is_staff


class ProjectView(ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = ProjectModel.objects.all()
    serializer_class = ProjectModelSerializers
    # pagination_class = MyPaginator
    filterset_class = ProjectFilter


class TodoView(UpdateModelMixin, CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, ListModelMixin, GenericViewSet):
    queryset = TodoModel.objects.all()
    serializer_class = TodoModelSerializers
    # pagination_class = MyPaginatorTodoView
    filterset_class = TodoFilter

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        print(instance.is_active)
        instance.is_active = False
        print(instance.is_active)
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

