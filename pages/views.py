from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Page
from .forms import PageForm


class PageDetailView(DetailView):
    model = Page

class PageListView(ListView):
    model = Page

class PageCreate(CreateView):
    model = Page
    form_class = PageForm
    # fields = ['title', 'content', 'ordering']
    success_url = reverse_lazy('pages:pages')

class PageDelete(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')

class PageUpdate(UpdateView):
    model = Page
    fields = ['title', 'content', 'ordering']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('pages:page', args=[self.object.id]) + '?ok'