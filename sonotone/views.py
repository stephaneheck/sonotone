# Create your views here.
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext, loader
from django.views.generic import ListView, DetailView, FormView, CreateView

from sonotone.models import Album, Contact
from sonotone.forms import ContactForm


class AlbumView(DetailView):
    model = Album

    def dispatch(self, request, *args, **kwargs):
        self.album = Album.objects.get(id=kwargs['album_id'])
        return super(AlbumView, self).dispatch(request, *args, **kwargs)

    def get_object(self):
        return self.album


class AlbumListView(ListView):
    model = Album


def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        album_list = Album.objects.filter(name__icontains=q)
        template = loader.get_template('sonotone/album_list.html')
        context = RequestContext(request, {'album_list': album_list, })
        return HttpResponse(template.render(context))
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            watcher = Contact(email=cd['email'], surname=cd['surname'], firstname=cd['firstname'])
            watcher.save()
            return HttpResponseRedirect('sonotone/thanks/')
    else:
        form = ContactForm()
    return render(request, 'sonotone/contact_form.html', {'form': form})


class ContactView(DetailView):
    model = Contact

    def dispatch(self, request, *args, **kwargs):
        self.contact = Contact.objects.get(id=kwargs['contact_id'])
        return super(ContactView, self).dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        args = super(ContactView, self).get_form_kwargs()
        args['request_country'] = self.request.COUNTRY_CODE
        return args

    def get_object(self):
        return self.contact


class ContactListView(ListView):
    # TODO : Contact.objects.order_by('-email')
    model = Contact


class ContactCreateView(CreateView):
    form_class = ContactForm
    model = Contact
    template_name = "sonotone/contact_form.html"





