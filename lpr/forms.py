from django import forms
from .models import lpr
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class LPRForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LPRForm, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)

        # You can dynamically adjust your layout
        self.helper.layout.append(Submit('save', 'save'))

    class Meta:
        model = lpr
        exclude = ['timestamp']
