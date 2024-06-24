from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.notes_main, name='notes_main'),
    path('add_tag/', views.add_tag, name='add_tag'),
    path('add_note/', views.note_add, name='note_add'),
    path('note_update/<int:pk>/', views.note_update, name='note_update'),
    path('delete/<int:pk>/', views.delete_note, name='delete_note'),
]
