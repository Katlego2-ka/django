# views.py
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse

def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(
           reverse('user_auth:login')
        ) 
    else:
        login(request, user)
        return HttpResponseRedirect(
           reverse('user_auth:show_user')
        )


