from django.urls import path, include

from . import views

app_name = "my_files"

urlpatterns = [

    path('upload/', views.upload_file, name='upload_file'),
    path('file/', views.file_list, name='file_list'),
    path('delete/<int:pk>/', views.delete_file, name='delete_file'),

]