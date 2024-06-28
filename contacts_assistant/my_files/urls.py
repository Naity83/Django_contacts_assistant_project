from django.urls import path, include

from . import views

app_name = "my_files"

urlpatterns = [
    path('', views.main, name='home'),
    path('upload_picture/', views.upload_picture, name='upload_picture'),
    path('upload_video/', views.upload_video, name='upload_video'),
    path('upload_document/', views.upload_document, name='upload_document'),
    path('remove_picture/<int:pk>/', views.remove_picture, name='remove_picture'),
    path('change_picture/<int:pk>/', views.change_picture, name='change_picture'),
    path('video/<int:pk>/remove/', views.remove_video, name='remove_video'),
    path('video/<int:pk>/change/', views.change_video, name='change_video'),
    path('remove_document/<int:pk>/', views.remove_document, name='remove_document'),
    path('change_document/<int:pk>/', views.change_document, name='change_document'),
    path('filter_picture', views.filter_picture, name='filter_picture'),
    path('filter_video', views.filter_video, name='filter_video'),
    path('filter_document', views.filter_document, name='filter_document'),

]