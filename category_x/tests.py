from django.test import TestCase, Client
from django.urls import reverse


class TestUrlResolve(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index(self):
        res = self.client.get(reverse("category_x:index"))
        self.assertEqual(200, res.status_code)

    def test_resolve_url_to_template(self):
        for template_name in ("aa", "bb"):
            with self.subTest(tn=template_name):
                url = reverse("category_x:static_render",
                              kwargs=dict(template_name=template_name))
                res = self.client.get(url)
                self.assertEqual("/category-x/{}/".format(template_name), url)
                self.assertEqual(200, res.status_code)
