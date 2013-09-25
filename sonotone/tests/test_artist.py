from django.db import IntegrityError

from django.test import TestCase
from sonotone.models import Artist


class ArtistTestCase(TestCase):
    def setUp(self):
        Artist.objects.create(name="John Bon Jovi")
        Artist.objects.create(name="Led Zeppelin")

    def test_artist_name_is_unique(self):
        with self.assertRaises(IntegrityError):
            Artist.objects.create(name="Led Zeppelin")