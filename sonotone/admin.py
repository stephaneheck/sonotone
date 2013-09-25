__author__ = 'sheck'

from django.contrib import admin
from sonotone.models import Artist,Style,Album

admin.site.register(Artist)
admin.site.register(Style)
admin.site.register(Album)
