from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
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

    context['project_form'] = ProjectForm()
    context['well_form'] = WellForm()
    context['projects'] = Project.objects.all()
    context['steps'] = Step.objects.all()
    context['sequence'] = Sequence.objects.all()

    return render(request, 'main/index.html', context)


@login_required
def lookahead(request):
    context = {}

    if request.method == 'POST' and "delete_project" in request.POST:
        project_id = request.POST.get("delete_project")
        project = Project.objects.get(pk=project_id)
        if project.created_by == request.user:
            messages.success(request, f'{project.name} project successfully deleted.')
            project.delete()
        return redirect(request.path)

    context['projects'] = Project.objects.all()
    context['steps'] = Step.objects.all()
    context['sequence'] = Sequence.objects.all()

    return render(request, 'main/lookahead.html', context)


@login_required
def crud_project(request):
    if request.method == 'POST' and "create_project" in request.POST:
        project_form = ProjectForm(request.POST)
        if project_form.is_valid():
            project = project_form.save(commit=False)
            project.created_by = request.user
            project.save()
            n = request.POST.get('next')
            messages.success(request, f'{project_form["name"].value()} project successfully created.')
            return HttpResponseRedirect(n)

    if request.method == 'POST' and "delete_project" in request.POST:
        project_id = request.POST.get("project_id")
        project = Project.objects.get(pk=project_id)
        if project.created_by == request.user:
            messages.success(request, f'{project.name} project successfully deleted.')
            project.delete()
            n = request.POST.get('next')
            return HttpResponseRedirect(n)


@login_required
def crud_well(request):
    if request.method == 'POST' and "create_well" in request.POST:
        well_form = WellForm(request.POST)
        if well_form.is_valid():
            well = well_form.save(commit=False)
            well.created_by = request.user
            project_id = request.POST.get("project_id")
            project = Project.objects.get(pk=project_id)
            well.project = project
            well.save()
            n = request.POST.get('next')
            messages.success(request, f'{well_form["name"].value()} well successfully created.')
            return HttpResponseRedirect(n)

    if request.method == 'POST' and "delete_well" in request.POST:
        well_id = request.POST.get("well_id")
        well = Well.objects.get(pk=well_id)
        if well.created_by == request.user:
            messages.success(request, f'{well.name} well successfully deleted.')
            well.delete()
            n = request.POST.get('next')
            return HttpResponseRedirect(n)
