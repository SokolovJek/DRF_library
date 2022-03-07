from django.shortcuts import render
from .models import Author
from .serializers import AuthorsModelSerializers
from rest_framework.viewsets import ModelViewSet


class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorsModelSerializers


