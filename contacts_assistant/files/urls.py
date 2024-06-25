# from django.urls import path, include
#
# from . import views
#
# app_name = "files"
#
# urlpatterns = [
#     path('', views.index, name='home'),
#     path('all_my_files/', views.all_files, name='all_my_files'),
#     path('upload/', views.upload, name='upload_file')
# ]


from django.urls import path
from .views import upload_file, file_list, delete_file

app_name = "files"

urlpatterns = [
    path('upload/', upload_file, name='upload_file'),
    path('files/', file_list, name='file_list'),
    path('delete/<int:pk>/', delete_file, name='delete_file'),
]
