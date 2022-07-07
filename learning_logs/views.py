from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.http import Http404

# Create your views here.
def index(request):
    """homepage"""
    return render(request, 'learning_logs/index.html')


@login_required
def topics(request):
    """Список тем"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


@login_required
def topic(request, topic_id):
     """ Enter one topic and few outsides topics"""
     topic = Topic.objects.get(id = topic_id)
     """check that the topic belongs to the current user"""
     if topic.owner != request.user:
         raise Http404
     entries = topic.entry_set.order_by('-date_added')
     topics = Topic.objects.filter(owner=request.user).order_by('date_added')
     context = {'topic': topic, 'entries': entries}
     return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request):
    """new topic creare"""
    if request.method != 'POST':
        #if date no send: create form
        form = TopicForm()
    else:
        #Send date POST: process data
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            #form.save()
            return redirect('learning_logs:topics')
    #output an empty or invalid form
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    """add new entry on a specific topic"""
    topic = Topic.objects.get(id=topic_id)
    if request.method !='POST':
        #data no send, create entry form
        form = EntryForm()
    else:
        #send data POST, process
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.topic = topic
            new_topic.save()
            return redirect('learning_logs:topic', topic_id=topic_id)
    #output an empty or invalid form
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    "edit entry"
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        #send data POST, process data
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)
    context = {'entry': entry, 'topic':topic, 'form':form}
    return render(request, 'learning_logs/edit_entry.html', context)