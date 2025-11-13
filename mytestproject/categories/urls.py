from django.urls import path
from . import views

urlpatterns = [
    # path('',views.hello,name='home'),
    path('',views.get,name='categories'),#вывод заметок
    path('<int:id>/',views.show,name='category'),
    path('add/',views.add, name='category_create'),
    path('update/<int:id>/',views.update,name='update_category'),
    path('delete/<int:id>',views.delete, name='delete_category')
]