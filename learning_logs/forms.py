from django import forms
from .models import Entry, Topic

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic # Model
        fields = ['text'] # Campos do formulário
        labels = {'text': ''} # Inicia o campo text vazio sem rótulo
    
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}