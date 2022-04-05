from django.shortcuts import render
from .models import Author
from .serializers import AuthorsModelSerializers
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import mixins


class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorsModelSerializers


# class AuthorModelViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, GenericViewSet):
#     queryset = Author.objects.all()
#     serializer_class = AuthorsModelSerializers

