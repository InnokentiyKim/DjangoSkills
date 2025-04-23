from email.policy import default

from django.core.management import BaseCommand
from shopapp.models import Product, Order
from django.db.models import Avg, Max, Min, Sum, Count


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Starting demo aggregate")
        result = Product.objects.aggregate(
            Avg("price"),
            Min("price"),
            Max("price"),
            Sum("price"),
            Count("id"),
        )
        print(result)

        orders = Order.objects.annotate(
            total=Sum("products__price", default=0),
            products_count = Count("products"),
        )
        for order in orders:
            print(f"Order #{order.id} with {order.products_count} products worth {order.total}")
        self.stdout.write(self.style.SUCCESS("Done"))