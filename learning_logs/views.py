


from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import is_valid_path, reverse

import learning_logs

from .models import Topic
from .forms import TopicForm, EntryForm

# Create your views here.
def index(request):
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Show all topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """Show only topic and all yours informations"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic,
               'entries': entries}
    return render(request, 'learning_logs/topic.html', context)



def new_topic(request):
    """Add a new Topic """
    if request.method != 'POST':
        form = TopicForm() # Create a form
    else:
        # POST
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))
    context = {'form':form}

    return render(request, 'learning_logs/new_topic.html', context)


def new_entry(request, topic_id):
    """Add a new entry of a topic"""
    topic = Topic.objects.get(id=topic_id)

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