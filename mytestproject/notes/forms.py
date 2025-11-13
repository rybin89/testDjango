# формы добавления и удаления записей
from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title','body'] # Поля для добавления ЗАМЕТОК, Зогловок и Текст

