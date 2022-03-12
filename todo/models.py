from django.db import models
from authors.models import Author
from uuid import uuid4


class ProjectModel(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid4)
    project_name = models.CharField(max_length=100)
    users = models.ManyToManyField(Author)
    link_git = models.URLField()
    descriptions = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'проэкт - {self.project_name}'


class TodoModel(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid4)
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE)
    todo_descriptions = models.TextField()
    users = models.ForeignKey(Author,
                              models.SET_NULL,
                              blank=True,
                              null=True)
    is_active = models.BooleanField(default=True)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.todo_descriptions
