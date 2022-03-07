from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework import serializers
from .models import ProjectModel, TodoModel
from authors.serializers import AuthorsModelSerializers


class ProjectModelSerializers(serializers.ModelSerializer):
    # users = serializers.StringRelatedField(many=True)

    class Meta:
        model = ProjectModel
        exclude = ['uid']


class TodoModelSerializers(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = TodoModel
        fields = '__all__'
