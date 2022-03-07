from django.shortcuts import render
from .models import ProjectModel, TodoModel
from .serializers import ProjectModelSerializers, TodoModelSerializers
from rest_framework.viewsets import ModelViewSet


class ProjectView(ModelViewSet):
    queryset = ProjectModel.objects.all()
    serializer_class = ProjectModelSerializers




class TodoView(ModelViewSet):
    queryset = TodoModel.objects.all()
    serializer_class = TodoModelSerializers
