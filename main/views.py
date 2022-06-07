from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import *

# Create your views here.


def index(request):
    # return HttpResponse("<h1>Hi Joachim, this is the main page.</h1>")
    context = {}
    messages.set_level(request, messages.DEBUG)
    # messages.debug(request, 'This is DEBUG.')
    # messages.info(request, 'This is INFO.')
    # messages.success(request, 'This is SUCCESS.')
    # messages.warning(request, 'This is WARNING.')
    # messages.error(request, 'This is ERROR.')

    if "create_project" in request.POST and request.method == 'POST':
        project_form = ProjectForm(request.POST)
        if project_form.is_valid():
            project_form.save()
            messages.success(request, f'{project_form["project_name"].value()} project successfully created.')
        return redirect(index)
    project_form = ProjectForm()
    context['project_form'] = project_form

    projects = Project.objects.all()
    context['projects'] = projects

    return render(request, 'main/index.html', context)
