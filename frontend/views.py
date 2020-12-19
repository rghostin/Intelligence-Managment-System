from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, CreateView, FormView

from frontend.forms import IntelCreationForm
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


@method_decorator(login_required, name='dispatch')
class IntelCreate(CreateView):
    model = Intel
    form_class = IntelCreationForm
    template_name = "frontend/intel_create.html"

    def form_valid(self, form):
        print(self.request.POST)
        intel = form.save(commit=False)
        intel.author = self.request.user
        intel.save()
        files = self.request.FILES.getlist('files_field')
        for f in files:
            IntelFile.objects.create(intel=intel, file=f)
        messages.success(self.request, "Intel created successfully")
        return redirect('view', pk=intel.id)

