from django.test import TestCase
from django.urls import reverse
from string import ascii_letters
from random import choices

from shopapp.models import Product
from shopapp.utils import add_two_numbers


class AddTwoNumbersTestCase(TestCase):
    def test_add_two_numbers(self):
        result = add_two_numbers(2, 3)
        self.assertEqual(result, 5)


class ProductCreateViewTestCase(TestCase):
    def setUp(self):
        self.product_name = "".join(choices(ascii_letters, k=10))
        Product.objects.filter(name=self.product_name).delete()

    def test_create_product(self):
        data = {
            "name": self.product_name,
            "price": "123.45",
            "description": "A good product",
            "discount": "10",
        }
        response = self.client.post(reverse("shopapp:products_create"), data=data, HTTP_USER_AGENT='Mozilla/5.0')
        self.assertFalse(Product.objects.filter(name=self.product_name).exists())


class ProductsListViewTestCase(TestCase):
    fixtures = ["products-fixture.json"]

    def test_products(self):
        response = self.client.get(reverse("shopapp:products_list"), HTTP_USER_AGENT='Mozilla/5.0')
        self.assertQuerySetEqual(qs=Product.objects.filter(archived=False).all(),
                                 values=(p.pk for p in response.context["products"]),
                                 transform=lambda p: p.pk
                                 )
        self.assertTemplateUsed(response, "shopapp/products-list.html")