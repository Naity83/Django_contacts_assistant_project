from django.urls import path
from . import views

app_name = "my_files"

urlpatterns = [
    path('', views.main, name='home'),
    path('<int:page>/', views.main, name='root_paginate'),
    path('upload_picture/', views.upload_picture, name='upload_picture'),
    path('upload_video/', views.upload_video, name='upload_video'),
    path('upload_document/', views.upload_document, name='upload_document'),
    path('remove_picture/<int:pk>/', views.remove_picture, name='remove_picture'),
    path('change_picture/<int:pk>/', views.change_picture, name='change_picture'),
    path('video/<int:pk>/remove/', views.remove_video, name='remove_video'),
    path('video/<int:pk>/change/', views.change_video, name='change_video'),
    path('remove_document/<int:pk>/', views.remove_document, name='remove_document'),
    path('change_document/<int:pk>/', views.change_document, name='change_document'),
    path('filter_picture/<int:page>/', views.filter_picture, name='filter_picture'),  # Проверьте наличие этого пути
    path('filter_video/<int:page>/', views.filter_video, name='filter_video'),
    path('filter_document/<int:page>/', views.filter_document, name='filter_document'),
    path('remove_picture_filter/<int:pk>/', views.remove_picture_filter, name='remove_picture_filter'),
    path('video/<int:pk>/remove_filter/', views.remove_video_filter, name='remove_video_filter'),
    path('remove_document_filter/<int:pk>/', views.remove_document_filter, name='remove_document_filter'),
]


