from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Section, Model
from .forms import SectionForm, ModelForm
from django.http import Http404


def index(request):
    """Homepage"""
    return render(request, 'learning_logs/index.html')


@login_required
def sections(request):
    """Get a list of topics from db related to a specific user"""
    sections = Section.objects.filter(owner=request.user).order_by('date_added')
    context = {'sections': sections}
    return render(request, 'learning_logs/sections.html', context)


@login_required
def section(request, section_id):
    """One particular topic is displayed, so an exception is thrown
    if this topic is not owned by the current user
    and display all messages related to the topic in reverse order"""
    section = Section.objects.get(id=section_id)
    if section.owner != request.user:
        raise Http404
    models = section.model_set.order_by('-date_added')
    context = {'section': section, 'models': models}
    return render(request, 'learning_logs/section.html', context)


@login_required
def model(request, model_id):
    model = Model.objects.get(id=model_id)
    return render(request, 'learning_logs/model.html', {'model': model})


@login_required
def new_section(request):
    """Adding new topic with help form and
    check that the added topic is associated with the current user"""
    if request.method != 'POST':
        form = SectionForm()
    else:
        form = SectionForm(data=request.POST)
        if form.is_valid():
            new_section = form.save(commit=False)
            new_section.owner = request.user
            new_section.save()
            return redirect('learning_logs:sections')
    context = {'form': form}
    return render(request, 'learning_logs/new_section.html', context)


@login_required
def new_model(request, section_id):
    """Add an entry, do not associate with the current user,
    since the entries are associated with topics and
    will automatically be associated"""
    section = Section.objects.get(id=section_id)
    if request.method != 'POST':
        form = ModelForm()
    else:
        form = ModelForm(request.POST, request.FILES)
        if form.is_valid():
            new_model = form.save(commit=False)
            new_model.section = section  # save with need topic
            new_model.save()
            return redirect('learning_logs:section', section_id=section_id)
    context = {'section': section, 'form': form}
    return render(request, 'learning_logs/new_model.html', context)


@login_required
def edit_model(request, model_id):
    """We get the necessary record from the database with the necessary information,
    if not associated with the current user, throw an exception,
    if all checks passed, save to the database with changes
    """
    model = Model.objects.get(id=model_id)
    section = model.section
    if section.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = ModelForm(instance=model)
    else:
        form = ModelForm(instance=model, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:section', section_id=section.id)
    context = {'model': model, 'section': section, 'form': form}
    return render(request, 'learning_logs/edit_model.html', context)


@login_required
def edit_section(request, section_id):
    """We get the necessary record from the database with the necessary information,
    if not associated with the current user, throw an exception,
    if all checks passed, save to the database with changes
    """
    section = Section.objects.get(id=section_id)
    if section.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = SectionForm(instance=section)
    else:
        form = SectionForm(instance=section, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:section', section_id=section.id)
    context = {'section': section, 'form': form}
    return render(request, 'learning_logs/edit_section.html', context)


@login_required
def delete_section(request, section_id):
    """Ge get the topic from the database and delete it"""
    section = Section.objects.filter(id=section_id).delete()
    return redirect('learning_logs:sections')


@login_required
def delete_all_sections(request):
    """Get the all topics from the database and delete it"""
    section = Section.objects.all().delete()
    return redirect('learning_logs:sections')


@login_required
def delete_model(request, model_id):
    """We get the entry from the database and delete it"""
    model = Model.objects.get(id=model_id)
    section_id = model.section.id
    model.delete()
    return redirect('learning_logs:section', section_id)
