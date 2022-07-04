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
                'placeholder': 'Project name'
            }),
        }


class WellForm(ModelForm):
    class Meta:
        model = Well
        fields = ['name', ]
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Well name'
            }),
        }


class PhaseForm(ModelForm):
    class Meta:
        model = Phase
        fields = ['name', ]
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phase'
            }),
        }


class StepForm(ModelForm):
    class Meta:
        model = Step
        fields = ['ops_step', ]
        widgets = {
            'ops_step': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Step description'
            }),
        }


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
