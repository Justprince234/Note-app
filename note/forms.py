from django import forms

from .models import Topic, Note

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['topic']

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['note']