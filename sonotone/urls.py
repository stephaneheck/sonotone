from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from sonotone import views
from sonotone.views import AlbumListView, AlbumView, ContactListView, ContactView, ContactCreateView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sonotone.views.home', name='home'),
    # url(r'^sonotone/', include('sonotone.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # ex: /album/5/
    url(r'^albums/(?P<album_id>\d+)/$', AlbumView.as_view(), name='album_detail'),
    # albums
    #url(r'^albums/', views.albums, name='albums'),
    url(r'^albums/', AlbumListView.as_view(),name='albums'),

    # ex: general search/
    (r'^search/$', views.search),

    # contacts
    url(r'^contacts/(?P<contact_id>\d+)/$', ContactView.as_view(), name='contact_detail'),
    url(r'^contacts/add/$', ContactCreateView.as_view(), name='contact_form'),
    url(r'^contacts/$', ContactListView.as_view(), name='contact_list'),


    # default
    #url(r'^', views.albums, name='albums'),


)
