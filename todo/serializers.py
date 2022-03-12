from rest_framework import serializers
from .models import ProjectModel, TodoModel


class ProjectModelSerializers(serializers.HyperlinkedModelSerializer):
    set_todo = serializers.SerializerMethodField()

    class Meta:
        model = ProjectModel
        fields = '__all__'

    def get_set_todo(self, obj):
        a = []
        for i in TodoModel.objects.filter(project=obj.pk):
           a.append(str(i))
        return a


class TodoModelSerializers(serializers.HyperlinkedModelSerializer):
    project = serializers.StringRelatedField()
    users = serializers.StringRelatedField()

    class Meta:
        model = TodoModel
        fields = '__all__'
