
from django.core.management import BaseCommand
from shopapp.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Starting demo select fields")
        product_values = Product.objects.values("pk", "name")
        for item in product_values:
            print(item)
        self.stdout.write(self.style.SUCCESS("Done"))