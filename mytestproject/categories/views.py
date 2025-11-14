from django.shortcuts import render, get_object_or_404, redirect
from .models import Category
from .forms import CategoryForm
# Create your views here.
# За фунционал и вывод в браузер/api
# Метод вывода заметок
def get(request):
    categories = Category.objects.all() # Получаем список из БД в переменную categories
    # передать спиcок в html-страницу
    return render(request,'category/categories.html',{'categories':categories})

# Метод вывода одной категории
def show(request,id):
    category = get_object_or_404(Category,pk=id) # category присваивается объект из таблицы с id == id
    # передать category в html-страницу
    return render(request,'category/category.html', {'category':category})

# Удалить записб
def delete(request,id):
    category = get_object_or_404(Category,pk=id)
    category.delete()
    return redirect('categories')

# Добавить
def add(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = CategoryForm()
    return render(request,'category/forms.py.html',{
        'form':form, 'title_page': 'Создать Категорию'
    })
# Обновить
def update(request,id):
    category = get_object_or_404(Category,pk=id)
    if request.method == 'POST':
        form = CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            return redirect('category',id=id)
    else:
        form = CategoryForm(instance=category)
    return render(request,'category/forms.py.html',{
        'form':form, 'title_page': 'Изменить Категорию'
    })