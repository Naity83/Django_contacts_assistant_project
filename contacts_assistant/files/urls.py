from django.urls import path, include

from . import views

app_name = "files"

urlpatterns = [
    path('', views.index, name='home'),
    path('all_my_files/', views.all_files, name='all_my_files'),
    path('upload/', views.upload, name='upload_file')
]
