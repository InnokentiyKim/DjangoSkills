from django.core.management import BaseCommand

from shopapp.models import Order, Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Updating order")
        order = Order.objects.first()
        if not order:
            self.stdout.write("Order not found")
            return
        products = Product.objects.all()
        for product in products:
            order.products.add(product)
        order.save()
        self.stdout.write(self.style.SUCCESS("Order successfully updated"))

