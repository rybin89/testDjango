from django.urls import path
from . import views

urlpatterns = [
    # path('',views.hello,name='home'),
    path('',views.notes,name='notes'),#вывод заметок
    path('<int:note_id>/',views.show,name='one_note'),
    path('add/',views.note_create, name='note_create'),
    path('update/<int:note_id>/',views.update,name='update'),
    path('delete/<int:note_id>',views.delete, name='delete')
]