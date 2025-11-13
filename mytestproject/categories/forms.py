# формы добавления и удаления записей
from django import forms
from .models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category','description'] # Поля для добавления Ктегорий, Название и Описание

