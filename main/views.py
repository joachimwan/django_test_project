from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.contrib import messages
from django.db.models import Max
from django.forms import modelformset_factory
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
    context['lookahead_form'] = LookaheadForm()
    context['projects'] = Project.objects.all()

    return render(request, 'main/index.html', context)


@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def well(request):
    context = {
        'projects': Project.objects.all(),
        'phase_form': PhaseForm(),
        'step_form': StepForm()
    }
    return render(request, 'main/well.html', context)


@login_required
def lookahead(request):
    context = {
        'projects': Project.objects.all(),
    }
    return render(request, 'main/lookahead.html', context)


@login_required
def test(request):
    context = {}

    well_x = Well.objects.all().first()
    test_x = Phase.objects.filter(well=well_x)
    value_x = test_x.aggregate(Max('order'))["order__max"]
    messages.success(request, f'test test {value_x} test test')

    # formset tests
    ProjectFormSet = modelformset_factory(Project, ProjectForm, extra=3)
    if request.method == 'POST':
        formset = ProjectFormSet(request.POST, queryset=Project.objects.filter(created_by=request.user))
        if formset.is_valid():
            for form in formset:
                if form.has_changed():
                    instance = form.save(commit=False)
                    instance.created_by = request.user
                    instance.save()
            return redirect(test)
        else:
            messages.warning(request, f'{ formset }')
    else:
        formset = ProjectFormSet(queryset=Project.objects.filter(created_by=request.user))
    context['formset'] = formset

    return render(request, 'main/test.html', context)


@login_required
def crud_project(request):
    if request.method == 'POST' and "create_project" in request.POST:
        project_form = ProjectForm(request.POST)
        n = request.POST.get('next')
        if project_form.is_valid():
            project = project_form.save(commit=False)
            project.created_by = request.user
            project.save()
            messages.success(request, f'{project_form["name"].value()} project successfully created.')
        else:
            messages.error(request, f'Unable to create {project_form["name"].value()} project.')
        return HttpResponseRedirect(n)

    if request.method == 'POST' and "delete_project" in request.POST:
        project_id = request.POST.get("project_id")
        n = request.POST.get('next')
        project = Project.objects.get(pk=project_id)
        if project.created_by == request.user:
            messages.success(request, f'{project.name} project successfully deleted.')
            project.delete()
            return HttpResponseRedirect(n)

    if request.method == 'POST' and "update_project" in request.POST:
        project_id = request.POST.get("project_id")
        n = request.POST.get('next')
        project = Project.objects.get(pk=project_id)
        if project.created_by == request.user:
            project_form = ProjectForm(request.POST, instance=project)
            if project_form.is_valid():
                project = project_form.save()
                messages.success(request, f'{project.name} project successfully updated.')
            else:
                messages.error(request, f'Unable to update {project.name} project.')
            return HttpResponseRedirect(n)


@login_required
def crud_well(request):
    if request.method == 'POST' and "create_well" in request.POST:
        well_form = WellForm(request.POST)
        n = request.POST.get('next')
        if well_form.is_valid():
            well = well_form.save(commit=False)
            well.created_by = request.user
            project_id = request.POST.get("project_id")
            project = Project.objects.get(pk=project_id)
            well.project = project
            well.save()
            messages.success(request, f'{well_form["name"].value()} well successfully created.')
        else:
            messages.error(request, f'Unable to create {well_form["name"].value()} well.')
        return HttpResponseRedirect(n)

    if request.method == 'POST' and "delete_well" in request.POST:
        well_id = request.POST.get("well_id")
        n = request.POST.get('next')
        well = Well.objects.get(pk=well_id)
        if well.created_by == request.user:
            messages.success(request, f'{well.name} well successfully deleted.')
            well.delete()
            return HttpResponseRedirect(n)

    if request.method == 'POST' and "update_well" in request.POST:
        well_id = request.POST.get("well_id")
        n = request.POST.get('next')
        well = Well.objects.get(pk=well_id)
        if well.created_by == request.user:
            well_form = WellForm(request.POST, instance=well)
            if well_form.is_valid():
                well = well_form.save()
                messages.success(request, f'{well.name} well successfully updated.')
            else:
                messages.error(request, f'Unable to update {well.name} well.')
            return HttpResponseRedirect(n)

    if request.method == 'POST' and "update_phase_order" in request.POST:
        well_id = request.POST.get("well_id")
        n = request.POST.get('next')
        well = Well.objects.get(pk=well_id)
        if well.created_by == request.user:
            for phase in well.phases.all():
                phase.order = request.POST.get(str(phase.id))
                phase.save()
            messages.success(request, f'{well.name} phase orders successfully updated.')
            return HttpResponseRedirect(n)


@login_required
def crud_phase(request):
    if request.method == 'POST' and "create_phase" in request.POST:
        phase_form = PhaseForm(request.POST)
        n = request.POST.get('next')
        if phase_form.is_valid():
            phase = phase_form.save(commit=False)
            well_id = request.POST.get("well_id")
            well = Well.objects.get(pk=well_id)
            phase.well = well
            order_max = Phase.objects.filter(well=well).aggregate(Max('order'))["order__max"]
            try:
                phase.order = order_max + 1
            except TypeError:
                phase.order = 1
            phase.save()
            messages.success(request, f'{phase_form["name"].value()} phase successfully created.')
        else:
            messages.error(request, f'Unable to create {phase_form["name"].value()} phase.')
        return HttpResponseRedirect(n)

    if request.method == 'POST' and "delete_phase" in request.POST:
        phase_id = request.POST.get("phase_id")
        n = request.POST.get('next')
        phase = Phase.objects.get(pk=phase_id)
        if phase.well.created_by == request.user:
            messages.success(request, f'{phase.name} phase successfully deleted.')
            phase.delete()
            return HttpResponseRedirect(n)

    if request.method == 'POST' and "update_phase" in request.POST:
        phase_id = request.POST.get("phase_id")
        n = request.POST.get('next')
        phase = Phase.objects.get(pk=phase_id)
        if phase.well.created_by == request.user:
            phase_form = PhaseForm(request.POST, instance=phase)
            if phase_form.is_valid():
                phase = phase_form.save()
                messages.success(request, f'{phase.name} phase successfully updated.')
            else:
                messages.error(request, f'Unable to update {phase.name} phase.')
            return HttpResponseRedirect(n)

    if request.method == 'POST' and "update_step_order" in request.POST:
        phase_id = request.POST.get("phase_id")
        n = request.POST.get('next')
        phase = Phase.objects.get(pk=phase_id)
        if phase.well.created_by == request.user:
            for step in phase.ops_steps.all():
                step.order = request.POST.get(str(step.id))
                step.save()
            messages.success(request, f'{phase.name} step orders successfully updated.')
            return HttpResponseRedirect(n)


@login_required
def crud_step(request):
    if request.method == 'POST' and "create_step" in request.POST:
        step_form = StepForm(request.POST)
        n = request.POST.get('next')
        if step_form.is_valid():
            step = step_form.save(commit=False)
            phase_id = request.POST.get("phase_id")
            phase = Phase.objects.get(pk=phase_id)
            step.phase = phase
            order_max = Step.objects.filter(phase=phase).aggregate(Max('order'))["order__max"]
            try:
                step.order = order_max + 1
            except TypeError:
                step.order = 1
            step.save()
            messages.success(request, f'{step_form["ops_step"].value()} step successfully created.')
        else:
            messages.error(request, f'Unable to create {step_form["ops_step"].value()} step.')
        return HttpResponseRedirect(n)

    if request.method == 'POST' and "delete_step" in request.POST:
        step_id = request.POST.get("step_id")
        n = request.POST.get('next')
        step = Step.objects.get(pk=step_id)
        if step.phase.well.created_by == request.user:
            messages.success(request, f'{step.ops_step} step successfully deleted.')
            step.delete()
            return HttpResponseRedirect(n)

    if request.method == 'POST' and "update_step" in request.POST:
        step_id = request.POST.get("step_id")
        n = request.POST.get('next')
        step = Step.objects.get(pk=step_id)
        if step.phase.well.created_by == request.user:
            step_form = StepForm(request.POST, instance=step)
            if step_form.is_valid():
                step = step_form.save()
                messages.success(request, f'{step.ops_step} step successfully updated.')
            else:
                messages.error(request, f'Unable to update {step.ops_step} step.')
            return HttpResponseRedirect(n)


@login_required
def crud_lookahead(request):
    if request.method == 'POST' and "create_lookahead" in request.POST:
        lookahead_form = LookaheadForm(request.POST)
        n = request.POST.get('next')
        if lookahead_form.is_valid():
            lookahead = lookahead_form.save(commit=False)
            lookahead.created_by = request.user
            project_id = request.POST.get("project_id")
            project = Project.objects.get(pk=project_id)
            lookahead.project = project
            lookahead.save()
            messages.success(request, f'{lookahead_form["name"].value()} lookahead successfully created.')
        else:
            messages.error(request, f'Unable to create {lookahead_form["name"].value()} lookahead.')
        return HttpResponseRedirect(n)

    if request.method == 'POST' and "delete_lookahead" in request.POST:
        lookahead_id = request.POST.get("lookahead_id")
        n = request.POST.get('next')
        lookahead = Lookahead.objects.get(pk=lookahead_id)
        if lookahead.created_by == request.user:
            messages.success(request, f'{lookahead.name} lookahead successfully deleted.')
            lookahead.delete()
            return HttpResponseRedirect(n)

    if request.method == 'POST' and "update_lookahead" in request.POST:
        lookahead_id = request.POST.get("lookahead_id")
        n = request.POST.get('next')
        lookahead = Lookahead.objects.get(pk=lookahead_id)
        if lookahead.created_by == request.user:
            lookahead_form = LookaheadForm(request.POST, instance=lookahead)
            if lookahead_form.is_valid():
                lookahead = lookahead_form.save()
                messages.success(request, f'{lookahead.name} lookahead successfully updated.')
            else:
                messages.error(request, f'Unable to update {lookahead.name} lookahead.')
            return HttpResponseRedirect(n)
