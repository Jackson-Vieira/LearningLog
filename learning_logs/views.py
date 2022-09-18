from datetime import datetime
from random import choice
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.urls import  reverse

from .models import Entry, Topic
from .forms import TopicForm, EntryForm

# Useful functions
def check_topic_owner(request, topic):
    if topic.owner != request.user:
        raise Http404


def index(request):
    """Home page"""

    user = request.user
    topics = []

    if user.is_anonymous == False:
        topics = Topic.objects.filter(
        owner=request.user,
        ).order_by('-date_added')
        num_pages = 1
        paginator = Paginator(topics, num_pages)
        page = request.GET.get('page')
        topics = paginator.get_page(page)

    return render(request, 'learning_logs/index.html', {'topics':topics})

@login_required
def topic(request, topic_id):
    """Show only topic and all yours informations"""
    topic = Topic.objects.get(id=topic_id)
    check_topic_owner(request, topic)

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic,
               'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def topics(request):
    random = bool(request.GET.get('random'))
    search_query = request.GET.get('search_query')

    topics = Topic.objects.all()

    if search_query != None:
        topics  = Topic.objects.filter(
            Q(entry__text__contains = search_query) | Q(title__contains = search_query),
        )#.distinct('entry') is not supported by SQLite3
        
    else:
        topics  = topics.filter(
            owner=request.user,
        ).order_by('date_added')

    if random:
        choice_topic = choice(topics)
        return topic(request, choice_topic.id)

    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


@login_required
def new_topic(request):
    """Add a new Topic """
    
    if request.method != 'POST':
        form = TopicForm() # Create a form
    else:
        # POST
        form = TopicForm(request.POST, request.FILES)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            form.save()

            return HttpResponseRedirect(reverse('learning_logs:topics'))

    template_name = 'learning_logs/new_topic.html'
    context = {'form':form}

    return render(request, template_name, context)

@login_required
def new_entry(request, topic_id):
    """Add a new entry of a topic"""
    topic = Topic.objects.get(id=topic_id)

    check_topic_owner(request, topic)

    if request.method != 'POST':
        """return a Empty forms"""
        form = EntryForm()
    
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))
    context = {'topic':topic,
               'form': form}
    return render(request,'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """Edit a existent entry of a topic"""

    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    check_topic_owner(request, topic)

    if request.method != 'POST':
        form = EntryForm(instance=entry)
        
    else:
        form = EntryForm(instance=entry, data=request.POST)
        entry.date_added = datetime.now()
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))

    context = {
            'entry':entry,
            'topic':topic,
            'form': form
               }

    return render(request,'learning_logs/edit_entry.html', context)