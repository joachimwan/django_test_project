from django.forms import ModelForm, TextInput
# from .models import Project, Well
from .models import *

# Create the form class.


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', ]
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. GK Phase 3'
            }),
        }


class WellForm(ModelForm):
    class Meta:
        model = Well
        fields = ['name', ]
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Miri-1'
            }),
        }


class PhaseForm(ModelForm):
    class Meta:
        model = Phase
        fields = ['name', 'well', ]


class StepForm(ModelForm):
    class Meta:
        model = Step
        fields = ['ops_step', 'phase', ]


class LookaheadForm(ModelForm):
    class Meta:
        model = Lookahead
        fields = ['name', ]
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control'
            }),
        }


class SequenceForm(ModelForm):
    class Meta:
        model = Sequence
        fields = ['lookahead', 'phase', ]
