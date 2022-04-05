from django.db import models
from uuid import uuid4


class Author(models.Model):
    # uid = models.UUIDField(primary_key=True, default=uuid4)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday_year = models.PositiveIntegerField()
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
