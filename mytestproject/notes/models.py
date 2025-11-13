from django.db import models

# Create your models here.
# ORM Django

class Note(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): # метод преобразования объекта в СТРОКУ
        return self.title # для admin-панели