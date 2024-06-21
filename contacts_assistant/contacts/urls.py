from django.urls import path, include

from . import views

app_name = "contacts"

urlpatterns = [
    path('', views.main, name='root'),  
    path('contacts/', views.contact_list, name='contact_list'),  # URL для списка контактов
    path('contacts/new/', views.contact_create, name='contact_create'),  # URL для создания нового контакта
    path('contacts/edit/<int:pk>/', views.contact_update, name='contact_update'),  # URL для редактирования контакта
    path('contacts/delete/<int:pk>/', views.contact_delete, name='contact_delete'),  # URL для удаления контакта
    path('upcoming_birthdays/<int:days>/', views.upcoming_birthdays, name='upcoming_birthdays'),  # URL для предстоящих дней рождения
    
   ]