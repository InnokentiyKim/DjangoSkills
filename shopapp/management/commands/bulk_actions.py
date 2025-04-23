
from django.core.management import BaseCommand
from shopapp.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Starting demo bulk actions")
        result = Product.objects.filter(
            name__contains="Smartphone"
        ).update(discount=10)
        print(result)
        # info = [
        #     ('Smartphone 1', 1999),
        #     ('Smartphone 2', 999),
        #     ('Smartphone 3', 1239),
        # ]
        # products = [
        #     Product(name=name, price=price)
        #     for name, price in info
        # ]
        # result = Product.objects.bulk_create(products)
        # for obj in result:
        #     print(obj)
        self.stdout.write(self.style.SUCCESS("Done"))