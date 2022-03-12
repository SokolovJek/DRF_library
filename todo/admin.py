from django.contrib import admin
from todo.models import ProjectModel, TodoModel
from authors.models import Author


# admin.site.register(Author)
admin.site.register(ProjectModel)
admin.site.register(TodoModel)
