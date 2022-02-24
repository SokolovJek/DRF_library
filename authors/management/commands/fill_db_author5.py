from django.core.management.base import BaseCommand
from authors.models import Author
import random


class Command(BaseCommand):
    def handle(self, *args, **options):
        Author.objects.all().delete()
        add_text = ['cx', 'oc', 'o', 'p', 'cc', 'ca', 'ac', 'xc', 'co', 'ko', 'cao']
        for i in range(5):
            random_text = add_text.pop(0)
            Author.objects.create(first_name=f'Евг{random_text}ений',
                                  last_name=f'Со{random_text}колов',
                                  birthday_year=random.randint(1990, 2020), email=f'sok{random_text}o@mail.ru')

