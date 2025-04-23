from typing import Sequence
from django.db import transaction
from django.contrib.auth.models import User
from django.core.management import BaseCommand
from shopapp.models import Order, Product


class Command(BaseCommand):
    @transaction.atomic
    def handle(self, *args, **options):
        self.stdout.write("Creating order with products")
        user = User.objects.get(username="admin")
        products = Product.objects.all()
        order, created = Order.objects.get_or_create(
            delivery_address="Moscow",
            promocode="12345",
            user=user,
        )
        for product in products:
            order.products.add(product)
        order.save()
        self.stdout.write(self.style.SUCCESS(f"Created order {order}"))