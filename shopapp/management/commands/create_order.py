from django.contrib.auth.models import User
from django.core.management import BaseCommand
from shopapp.models import Order


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Creating order")
        user = User.objects.get(username="admin")
        order = Order.objects.get_or_create(
            delivery_address="Moscow",
            promocode="123",
            user=user,
        )
        self.stdout.write(self.style.SUCCESS(f"Created order {order}"))