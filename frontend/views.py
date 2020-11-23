from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView, CreateView

from intelsAPI.filters import IntelFilter
from intelsAPI.models import Intel
from intelsAPI.serializers import IntelSerializer


def search(request):
    intelFilter = IntelFilter(request.GET, Intel.objects.all())
    print(intelFilter.form.fields['creation_date_range'])
    return render(request, 'frontend/search.html', locals())


class IntelView(DetailView):
    model = Intel
    template_name = 'frontend/resource_view.html'
    context_object_name = 'resource'


def intel_create(request):
    intel_serializer = IntelSerializer()
    return render(request, 'frontend/intel_create.html', locals())