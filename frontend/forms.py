
from django import forms

from intelsAPI.models import Intel


class IntelCreationForm(forms.ModelForm):
    files_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)

    class Meta:
        model = Intel
        fields = ['title', 'resource_type', 'description', 'tags', 'link', 'files_field', 'additional_note',
                  'text_content']

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': "Title"}),
            'description': forms.Textarea(attrs={'cols': 30, 'rows': 2}),
            'link': forms.URLInput(attrs={'placeholder': "https://example.com"}),
            'additional_note': forms.Textarea(attrs={'cols': 30, 'rows': 1}),
        }
