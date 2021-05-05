from django import forms
from createproject.models import Entry

class EntryForm(forms.ModelForm):

    class Meta:
        model = Entry