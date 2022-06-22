from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
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
            project = project_form.save(commit=False)
            project.created_by = request.user
            project.save()
            messages.success(request, f'{project_form["name"].value()} project successfully created.')
        return redirect(index)
    project_form = ProjectForm()
    context['project_form'] = project_form

    projects = Project.objects.all()
    context['projects'] = projects

    return render(request, 'main/index.html', context)


@login_required
def lookahead(request):
    context = {}

    if "delete_project" in request.POST and request.method == 'POST':
        project_id = request.POST.get("delete_project")
        project = Project.objects.get(pk=project_id)
        if project.created_by == request.user:
            messages.success(request, f'{project.name} project successfully deleted.')
            project.delete()
        return redirect(lookahead)

    projects = Project.objects.all()
    context['projects'] = projects

    steps = Step.objects.all()
    context['steps'] = steps

    sequence = Sequence.objects.all()
    context['sequence'] = sequence

    return render(request, 'main/lookahead.html', context)
