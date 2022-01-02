from django.http import response
from django.http.response import HttpResponse
from django.urls import reverse, resolve
from django.test import TestCase
from home.views import homepage

# Create your tests here.
class HomePageTest(TestCase):

    def test_root_url_resolve_to_home_page_view(self):
        # reverse：反查URL
        # resolve：解析
        found = resolve('/')
        self.assertEqual(found.func, homepage)

    def test_home_page_returns_correct_html(self):
        request = HttpResponse()
        response = homepage(request)
        self.asssertTrue(response.content.startswith(b'<html>'))
        self.asssertTrue(response.content.endswith(b'<html>'))