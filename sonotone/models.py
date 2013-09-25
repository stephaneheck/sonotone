from django.core.urlresolvers import reverse

__author__ = 'sheck'

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Artist(models.Model):
    name = models.CharField(_('Name'), max_length=256, unique=True)

    #object representation are used throughout Django generated admin
    def __unicode__(self):
        return self.name


class Style(models.Model):
    name = models.CharField(_('Name'), max_length=64, unique=True)

    #object representation are used throughout Django generated admin
    def __unicode__(self):
        return self.name


class Album(models.Model):
    artist = models.ForeignKey(Artist)
    name = models.CharField(_('Name'), max_length=256)
    release_date = models.DateTimeField(_('Release date'))
    style = models.ForeignKey(Style)

    # image = models.ImageField(_('Cover'), upload_to=upload_cover_image,
    #                           blank=True,
    #                           help_text=_('600x200px cover for this album.'))
    #
    # mini_image = ImageSpecField([ResizeToFit(120, 40),
    #                              ResizeCanvas(120, 40)],
    #                             image_field='image', format='PNG',
    #                             cache_to=cache_to)

    #object representation are used throughout Django generated admin
    def __unicode__(self):
        return str(self.artist) + ", " + self.name + ", " + str(self.release_date) + ", " + str(self.style)


    # def upload_cover_image(self):
    #     return u'{0}/image.png'.format(self.id.replace(':', '_'))





class Contact(models.Model):
    firstname = models.CharField(_('Firstname'), max_length=256)
    surname = models.CharField(_('Surname'), max_length=256)
    email = models.EmailField(_('Email'))

    def get_absolute_url(self):
        return reverse("contact_detail", kwargs={'contact_id': self.pk})

    #object representation are used throughout Django generated admin
    def __unicode__(self):
        output = _('Contact is %(firstname) %(surname), email: %s(email).') % {'firstname': self.firstname,
                                                                               'surname': self.surname,
                                                                               'email': self.email}
        return output


