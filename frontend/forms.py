from django import forms

from intelsAPI.models import Intel


class IntelCreationForm(forms.ModelForm):
    files_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)

    class Meta:
        model = Intel
        fields = ['title', 'resource_type', 'tags', 'link', 'files_field', 'additional_note', 'text_content']
