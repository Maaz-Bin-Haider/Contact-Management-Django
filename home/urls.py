from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addContact/',views.addContact, name='addContact'),
    path('searchContact/',views.searchContact, name='searchContact'),
    path('update/<int:contact_id>/', views.updateContact, name='updateContact'),
    path('delete/<int:contact_id>/', views.deleteContact, name='deleteContact'),
]