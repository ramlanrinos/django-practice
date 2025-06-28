from django.core.management.base import BaseCommand
from  blog.models import Category

class Command(BaseCommand):
    help = "This command inserts the categories data"

    def handle(self, *args, **options):
        categories = ["Science", "Technology", "Sports", "Art", "Food"]

        for categories_name in categories:
            Category.objects.create(name=categories_name)

        self.stdout.write(self.style.SUCCESS("Inserting data completed"))