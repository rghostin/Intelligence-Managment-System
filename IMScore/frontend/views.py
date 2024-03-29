from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from intelsAPI.bookmarker import Bookmarker
from frontend.forms import IntelCreationForm
from intelsAPI.filters import IntelFilter
from intelsAPI.models import Intel, IntelFile
from intelsAPI.views import assert_intel_author


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
    form_class = IntelCreationForm

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields.pop('files_field')
        return form

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        assert_intel_author(intel=obj, user=self.request.user)
        return obj

    def form_valid(self, form):
        print(self.request.POST)
        intel = form.save(commit=False)
        intel.author = self.request.user
        intel.save()
        form._save_m2m()
        messages.success(self.request, "Intel updated successfully")
        return redirect('view', pk=intel.id)


@method_decorator(login_required, name='dispatch')
class IntelDelete(DeleteView):
    model = Intel
    template_name = "frontend/intel_delete.html"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        assert_intel_author(intel=obj, user=self.request.user)
        return obj

    def get_success_url(self):
        intel = self.get_object()
        messages.warning(self.request, '#%s - %s has been deleted' % (intel.id, intel.title))
        return reverse("search")


@method_decorator(login_required, name='dispatch')
class BookmarkCreate(CreateView):
    model = Intel
    template_name = "frontend/bookmark_create.html"
    form_class = IntelCreationForm

    def get_form(self, form_class=None):
        form = super().get_form(form_class)

        to_exclude = ('resource_type', 'files_field', 'text_content')
        for field_name in to_exclude:
            form.fields.pop(field_name)

        form.fields['link'].required = True
        return form

    def form_valid(self, form):
        print(self.request.POST)
        intel = form.save(commit=False)
        intel.author = self.request.user
        intel.resource_type = "article"
        intel.save()
        form._save_m2m()

        try:
            Bookmarker.create_snapshot(intel=intel, link=intel.link)
        except Exception as e:
            intel.delete()
            messages.error(self.request, "Unable to create snapshot")
            return redirect('bookmark_create')

        messages.success(self.request, "Bookmark intel created successfully")
        return redirect('view', pk=intel.id)