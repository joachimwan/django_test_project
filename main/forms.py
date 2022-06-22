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
        fields = ['name', 'project', ]
