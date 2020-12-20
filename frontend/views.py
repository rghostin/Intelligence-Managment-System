from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from frontend.forms import IntelCreationForm
from intelsAPI.filters import IntelFilter
from intelsAPI.models import Intel, IntelFile


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
        form._save_m2m()
        files = self.request.FILES.getlist('files_field')
        for f in files:
            IntelFile.objects.create(intel=intel, file=f)
        messages.success(self.request, "Intel created successfully")
        return redirect('view', pk=intel.id)


@method_decorator(login_required, name='dispatch')
class IntelUpdate(UpdateView):
    model = Intel
    template_name = "frontend/intel_update.html"
    fields = ['title', 'resource_type', 'tags', 'link', 'additional_note', 'text_content']

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if self.request.user != obj.author:
            raise PermissionDenied
        return obj

    def form_valid(self, form):
        print(self.request.POST)
        intel = form.save(commit=False)
        intel.author = self.request.user
        intel.save()
        form._save_m2m()
        messages.success(self.request, "Intel updated successfully")
        return redirect('view', pk=intel.id)


class IntelDelete(DeleteView):
    model = Intel
    template_name = "frontend/intel_delete.html"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if self.request.user != obj.author:
            raise PermissionDenied
        return obj

    def get_success_url(self):
        intel = self.get_object()
        messages.warning(self.request, '#%s - %s has been deleted' % (intel.id, intel.title))
        return reverse("search")
