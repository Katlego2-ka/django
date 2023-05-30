
from django.urls import path, include
from django.contrib import admin
from . import views

app_name = 'user_auth'
urlpatterns = [
    path('authenticate_user/', views.authenticate_user,
name='authenticate_user')
]

