from django.urls import path, include
from . import views

urlpatterns = [
    
    path('about_candidate/', views.detail, name='about_candidate'),
    path('contacts/', views.results, name='contacts'),
    path('goal/', views.vote, name='goal'),
]