from email.mime import image
from django import forms
from .models import Entry, Topic

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic # Model
        fields = ('title', 'image', 'description') # Campos do formulário
        labels = {'title': 'Title', 'description':'Description', 'image':'Image'} # Inicia o campo text vazio sem rótulo
        widgets = {'description': forms.Textarea(attrs={'cols':80})}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}