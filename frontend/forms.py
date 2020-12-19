from django import forms

from intelsAPI.models import Intel


class IntelCreationForm(forms.ModelForm):
    files_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)

    class Meta:
        model = Intel
        exclude = ['author']
