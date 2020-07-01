from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages
from . models import Note, Topic
from .forms import TopicForm, NoteForm
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    """Displays the login page."""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('note:home')
        messages.info(request, 'Invalid Credentials.')
        return redirect('note:login')
    return render(request, 'note/login.html')

def logout(request):
    """Returns the logout page, redirecting to the home page."""
    auth.logout(request)
    return redirect('note:login')

@login_required
def home(request):
    """Displays the index page with Note and Topic database objects."""
    topics = Topic.objects.filter(owner=request.user)
    notes = Note.objects.all()
    context = {'notes': notes, 'topics': topics}
    return render(request, 'note/index.html', context)

@login_required
def add_topic(request):
    """ Adds a new topic to the database."""
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('note:home')

    return render(request, 'note/new_note.html')

@login_required
def topic_view(request, topic_id):
    """Dispays database objects from the Topic and Note tables."""
    topic = Topic.objects.get(id=topic_id)
    notes = topic.one.all()
    context = {'topic': topic, 'notes':notes}
    return render(request, 'note/topic_view.html', context)

@login_required
def add_note(request, topic_id):
    """Adds new note object to the database."""
    topic = Topic.objects.get(id = topic_id)             
    if request.method != 'POST':
        form = NoteForm()
    else:
        form = NoteForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
    
    return redirect(request.META['HTTP_REFERER'])

@login_required()
def update_note(request, note_id):
    """Updates the note object in the database."""
    new_entry = Note.objects.get(id=note_id)
    topic = new_entry.topic
    if request.method != 'POST':
        form = NoteForm(instance=new_entry)
    else:
        form = NoteForm(instance=new_entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('note:topic_view', topic_id=topic.id)
    context = {'new_entry': new_entry, 'topic': topic, 'form': form}
    return render(request, 'note/edit_entry.html', context)
    
@login_required
def delete(request, topic_id):
    """Deletes the Topic object from database."""
    topic_id = int(topic_id)
    del_topic = Topic.objects.get(id=topic_id)
    del_topic.delete()
    return redirect(request.META['HTTP_REFERER'])

@login_required
def search(request):
    """Searches the Topic object from database."""
    if 'q':
        template = 'note/search_details.html'
        query = request.GET.get('q')
        topic_results = Topic.objects.filter(Q(topic__icontains=query))
        context = {'topic_results': topic_results}

        return render(request, template, context)
    
    messages.info(request, 'No Record Found!')
    return redirect('note:home')
