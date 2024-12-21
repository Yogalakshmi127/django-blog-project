from blog.models import Category
from typing import Any
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "This command helps to insert category"
    def handle(self, *args, **options):
        Category.objects.all().delete()

        Categories = ['sports','Technology','Science','Arts','Food']

        for category_name in Categories:
            Category.objects.create(name = category_name)
        self.stdout.write(self.style.SUCCESS('Completed inserting data'))

