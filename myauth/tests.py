from django.test import TestCase
from django.urls import reverse


class GetCookieViewTestCase(TestCase):
    def test_get_cookie_view(self):
        response = self.client.get(path=reverse("myauth:cookie-get"), HTTP_USER_AGENT='Mozilla/5.0')
        self.assertContains(response, "Cookie value")


class FooBarViewTestCase(TestCase):
    def test_foo_bar_view(self):
        response = self.client.get(path=reverse("myauth:foo-bar"), HTTP_USER_AGENT='Mozilla/5.0')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], 'application/json')
        expected = {"foo": "bar", "spam": "eggs"}
        self.assertJSONEqual(response.content, expected)
