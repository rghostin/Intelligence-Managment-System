from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView, CreateView

from intelsAPI.filters import IntelFilter
from intelsAPI.models import Intel


def search(request):
    intelFilter = IntelFilter(request.GET, Intel.objects.all())
    print(intelFilter.form.fields['creation_date_range'])
    return render(request, 'frontend/search.html', locals())


class IntelView(DetailView):
    model = Intel
    template_name = 'frontend/resource_view.html'
    context_object_name = 'resource'


class IntelCreate(CreateView):
    model = Intel
    template_name = 'frontend/intel_create.html'
    fields = ['title', 'resource_type', 'tags', 'link', 'text_content', 'additional_note', ]

    def get_success_url(self):
        return reverse("view", kwargs={'pk':  self.object.pk})
