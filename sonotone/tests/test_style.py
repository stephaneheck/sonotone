from django.db import IntegrityError
from django.test import TestCase
from sonotone.models import Style


class StyleTestCase(TestCase):
    def setUp(self):
        Style.objects.create(name="ROCK")
        Style.objects.create(name="POP")

    def test_style_name_is_unique(self):
        with self.assertRaises(IntegrityError):
            Style.objects.create(name="POP")
