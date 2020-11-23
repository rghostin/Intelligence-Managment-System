from django.shortcuts import render
from django.views.generic import DetailView

from intelsAPI.filters import IntelFilter
from intelsAPI.models import Intel


def search(request):
    intelFilter = IntelFilter(request.GET, Intel.objects.all())
    print(intelFilter.form.fields)
    return render(request, 'frontend/search.html', locals())


class ResourceView(DetailView):
    model = Intel
    template_name = 'frontend/resource_view.html'
    context_object_name = 'resource'
