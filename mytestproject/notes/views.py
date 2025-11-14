from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import NoteForm
from .models import Note
# CRUD -
# Create your views here.
def hello(request): # request - объект запроса, вернуть объекта HTTP ответа
    return HttpResponse('Привет МИР!')

# Метод вывода заметок из БД
@login_required
def notes(request):
    notes = Note.objects.all() # Получаем все заметки из БД
    # html = '<h1>Тут будут заметки</h1>'
    # for note in notes:
    #     html += f'<a href = "/notes/{note.id}"><p>id = {note.id} title : {note.title} text: {note.body}</p></a>'
    # return HttpResponse(html)
    return render(request,'notes/notes.html',{'notes_html':notes})

# Методод вывода одной записи
@login_required
def show(request,note_id):
    note = get_object_or_404(Note,pk=note_id)
    # return HttpResponse(f'<h1>{note.title}</h1><p>{note.body}</p>')
    return render(request,'notes/one.html',{'note_html':note})

# Метод отабаражает ФОРМУ и Добавляет заметки в БД
@login_required
def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST) # получает данные которые ввели в форму
        if form.is_valid():
            form.save() # Записывает данные в таблицу БД
            return redirect('notes')
    else:
        form = NoteForm()
    return render(request,'notes/forms.py.html',{
        'form': form, 'title_page' : 'Создать заметку'
    })

# Обновление
@login_required
def update(request,note_id):
    note = get_object_or_404(Note,pk=note_id)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note) # instance=note будет заполнена данными из таблицы
        if form.is_valid():
            form.save()
            return redirect('one_note', note_id=note.id)
    else:
        form = NoteForm(instance=note)
    return render(request,'notes/forms.py.html',{
        'form':form, 'title_page' : 'Изменить заметку'
    })

# Удалить
def delete(request,note_id):
    note = get_object_or_404(Note,pk=note_id)
    note.delete()
    return redirect('notes')
