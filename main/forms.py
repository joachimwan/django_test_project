from django.forms import ModelForm
# from .models import Project, Well
from .models import *

# Create the form class.


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', ]


class WellForm(ModelForm):
    class Meta:
        model = Well
        fields = ['name', ]


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
        fields = ['name', 'project', ]


class SequenceForm(ModelForm):
    class Meta:
        model = Sequence
        fields = ['lookahead', 'phase', ]
