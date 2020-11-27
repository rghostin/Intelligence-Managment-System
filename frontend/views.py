from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, CreateView

from intelsAPI.filters import IntelFilter
from intelsAPI.models import Intel, IntelFile
from intelsAPI.serializers import IntelSerializer, IntelFileSerializer


@login_required
def search(request):
    intelFilter = IntelFilter(request.GET, Intel.objects.all())
    print(intelFilter.form.fields['creation_date_range'])
    return render(request, 'frontend/search.html', locals())


@method_decorator(login_required, name='dispatch')
class IntelView(DetailView):
    model = Intel
    template_name = 'frontend/intel_view.html'
    context_object_name = 'intel'


@login_required
def intel_create(request):
    intel_serializer = IntelSerializer()
    intelfile_serializer = IntelFileSerializer()
    return render(request, 'frontend/intel_create.html', locals())