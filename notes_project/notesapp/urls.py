from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.loginview,name='login'),
    path('delete_document/<int:docid>/',views.delete_document,name='delete_document'),
    path('register/',views.register,name='register'),
    # path('login/',views.loginview,name='login'),
    path('editor/',views.editor,name='editor'),
    path('logout/',views.logoutview,name='logout'),
]